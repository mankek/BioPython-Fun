#!/usr/bin/python
from Bio import Entrez, SeqIO
import os
import shutil
Entrez.email = "emailtestforkm@gmail.com"


def retrieve(db, acc_num, rettype):
    retmode = "text"
    for i in acc_num.split(","):
        filename = "App\\Files\\" + i + "." + rettype
        handle = Entrez.efetch(db=db, id=i, rettype=rettype, retmode=retmode)
        out_handle = open(filename, "w")
        out_handle.write(handle.read())
        out_handle.close()
        handle.close()
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


def upload(file_path):
    path = os.path.abspath(__file__)
    files_path = "\\".join(path.split("\\")[0:6])
    if os.path.exists(file_path):
        shutil.copyfile(file_path, os.path.join(files_path, "Files", file_path.split("\\")[-1]))
        return "done"
    else:
        return "File doesn't exist, uwu."


