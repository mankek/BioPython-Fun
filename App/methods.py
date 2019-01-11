#!/usr/bin/python
from Bio import Entrez, SeqIO
import os
import shutil
Entrez.email = "emailtestforkm@gmail.com"

global_record = {}
legal_rettypes = ["gp", "gb", "fasta"]


def get_db(db):
    db_dict = {"nuccore": "Nucleotide", "NA": "Not Available", "protein": "Protein"}
    return db_dict[db]


def retrieve(db, acc_num, rettype):
    retmode = "text"
    files_path = os.path.join("\\".join(os.path.abspath(__file__).split("\\")[0:-1]), "Files")
    for i in acc_num.split(","):
        filename = os.path.join(files_path, i.lstrip(" ") + "." + rettype)
        handle = Entrez.efetch(db=db, id=i, rettype=rettype, retmode=retmode, api_key="b88d297c7d1daf2c6d6c5a9a6efadcc82209")
        out_handle = open(filename, "w")
        out_handle.write(handle.read())
        out_handle.close()
        handle.close()
        global global_record
        global_record[i.lstrip(" ")] = {"db": get_db(db), "rettype": rettype}
    return "done"


def preview(db, acc_num, rettype):
    result = []
    retmode = "text"
    for i in acc_num.split(","):
        with Entrez.efetch(db=db, id=i.lstrip(" "), rettype=rettype, retmode=retmode, api_key="b88d297c7d1daf2c6d6c5a9a6efadcc82209") as handle:
            if rettype == "gp":
                parse_rettype = "gb"
            else:
                parse_rettype = rettype
            for seq_rec in SeqIO.parse(handle, parse_rettype):
                result.append({seq_rec.name: {"id": seq_rec.id, "description": seq_rec.description,
                                              "Sequence length": len(seq_rec), "features": len(seq_rec.features),
                                              "from": seq_rec.annotations["source"] if "source" in seq_rec.annotations.keys() else "NA"}})
    return result


def upload(file_path, db):
    path = os.path.abspath(__file__)
    files_path = "\\".join(path.split("\\")[0:6])
    if os.path.exists(file_path):
        if file_path.split("\\")[-1].split(".")[-1] in legal_rettypes:
            if db == "NA":
                db = guess_database(file_path)
            shutil.copyfile(file_path, os.path.join(files_path, "Files", file_path.split("\\")[-1]))
            global global_record
            if len(file_path.split("\\")[-1].split(".")) > 2:
                global_record[file_path.split("\\")[-1].split(".")[0] + "." + file_path.split("\\")[-1].split(".")[1]] = {"db": get_db(db), "rettype": file_path.split("\\")[-1].split(".")[-1]}
            else:
                global_record[file_path.split("\\")[-1].split(".")[0]] = {"db": get_db(db), "rettype": file_path.split("\\")[-1].split(".")[-1]}
            return "done"
        else:
            return "File doesn't have an accepted extension."
    else:
        print(file_path)
        return print("File doesn't exist.")


def get_files():
    files = []
    global global_record
    for s in global_record.keys():
        files.append(s + "." + global_record[s]["rettype"])
    path = os.path.abspath(__file__)
    files_path = "\\".join(path.split("\\")[0:6])
    files_path = os.path.join(files_path, "Files")
    for _,_,file_name in os.walk(files_path):
        for i in file_name:
            if i in files:
                continue
            elif i.split(".")[-1] not in legal_rettypes:
                continue
            else:
                i_path = os.path.join(files_path, i)
                i_rettype = i.split(".")[-1]
                db = guess_database(i_path)
                if len(i.split(".")) > 2:
                    global_record[i.split(".")[0] + "." + i.split(".")[1]] = {"db": get_db(db), "rettype": i_rettype}
                else:
                    global_record[i.split(".")[0]] = {"db": get_db(db), "rettype": i.split(".")[-1]}
    for t in files:
        if not os.path.exists(os.path.join(files_path, t)):
            if len(t.split(".")) > 2:
                global_record.pop(t.split(".")[0] + "." + t.split(".")[1])
            else:
                global_record.pop(t.split(".")[0])
        else:
            continue
    return "done"


def guess_database(file):
    file_rettype = file.split("\\")[-1].split(".")[-1]
    if file_rettype == "gp":
        file_rettype = "gb"
    for rec in SeqIO.parse(file, file_rettype):
        if rec.seq[0] == "M":
            return "protein"
        else:
            return "nuccore"


def comp(file_name, file_type, file_db):
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "Files", file_name + "." + file_type)
    if file_db == "Nucleotide":
        options = {"A": 0, "T": 0, "G": 0, "C": 0, "N": 0, "K": 0, "S": 0, "Y": 0, "M": 0, "W": 0, "R": 0, "B": 0,
                   "D": 0, "H": 0, "V": 0, "U": 0}
    elif file_db == "Protein":
        options = {"G": 0, "A": 0, "L": 0, "M": 0, "F": 0, "W": 0, "K": 0, "Q": 0, "E": 0, "S": 0, "P": 0, "V": 0,
                   "I": 0, "C": 0, "Y": 0, "H": 0, "R": 0, "N": 0, "D": 0, "T": 0, "X": 0}
    if file_type == "gp":
        file_type = "gb"
    for rec in SeqIO.parse(file_path, file_type):
        for s in range(0, len(rec.seq)):
            options[rec.seq[s]] += 1

    x = []
    for i in options.keys():
        if options[i] != 0:
            x.append(i)

    y = []
    for t in x:
        y.append(options[t])

    return x, y


def skew(file_name, file_type):
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "Files", file_name + "." + file_type)
    skew_val = [0]
    positions = []
    for rec in SeqIO.parse(file_path, file_type):
        for i in range(0, len(rec.seq)):
            positions.append(i)
            if (rec.seq[i] != "C") and (rec.seq[i] != "G"):
                skew_val.append(skew_val[len(skew_val) - 1])
            elif rec.seq[i] == "G":
                skew_val.append(skew_val[len(skew_val) - 1] + 1)
            elif rec.seq[i] == "C":
                skew_val.append(skew_val[len(skew_val) - 1] - 1)

    x = positions
    y = skew_val

    return x, y





