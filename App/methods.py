#!/usr/bin/python
from Bio import Entrez, SeqIO
import os
import shutil
Entrez.email = "emailtestforkm@gmail.com"

global_record = {}


def get_db(db):
    db_dict = {"nuccore": "Nucleotide", "NA": "Not Available"}
    return db_dict[db]


def retrieve(db, acc_num, rettype):
    retmode = "text"
    for i in acc_num.split(","):
        filename = "App\\Files\\" + i + "." + rettype
        handle = Entrez.efetch(db=db, id=i, rettype=rettype, retmode=retmode)
        out_handle = open(filename, "w")
        out_handle.write(handle.read())
        out_handle.close()
        handle.close()
        global global_record
        global_record[i] = {"db": get_db(db), "rettype": rettype}
    return "done"


def preview(db, acc_num, rettype):
    result = []
    retmode = "text"
    with Entrez.efetch(db=db, id=acc_num, rettype=rettype, retmode=retmode) as handle:
        for seq_rec in SeqIO.parse(handle, rettype):
            result.append({seq_rec.name: {"id": seq_rec.id, "description": seq_rec.description,
                                          "Sequence length": len(seq_rec), "features": len(seq_rec.features),
                                          "from": seq_rec.annotations["source"]}})
    return result


def upload(file_path, db):
    path = os.path.abspath(__file__)
    files_path = "\\".join(path.split("\\")[0:6])
    if os.path.exists(file_path):
        shutil.copyfile(file_path, os.path.join(files_path, "Files", file_path.split("\\")[-1]))
        global global_record
        global_record[file_path.split("\\")[-1].split(".")[0]] = {"db": get_db(db), "rettype": file_path.split("\\")[-1].split(".")[-1]}
        return "done"
    else:
        return "File doesn't exist, uwu."


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
            else:
                global_record[i.split(".")[0]] = {"db": "Not Available", "rettype": i.split(".")[-1]}
    for t in files:
        if not os.path.exists(os.path.join(files_path, t)):
            global_record.pop(t.split(".")[0])
        else:
            continue
    return "done"





