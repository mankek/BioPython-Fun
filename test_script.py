#!/usr/bin/python
from Bio import SeqIO
import plotly.plotly as pl
import plotly.graph_objs as go


def skew_plot(fasta_file):
    skew = [0]
    positions = []
    for record in SeqIO.parse(fasta_file, "fasta"):
        for i in range(0, len(record.seq)):
            positions.append(i)
            if (record.seq[i] == "A") or (record.seq[i] == "T"):
                skew.append(skew[len(skew)-1])
            elif record.seq[i] == "G":
                skew.append(skew[len(skew) - 1]+1)
            elif record.seq[i] == "C":
                skew.append(skew[len(skew) - 1]-1)

    trace = go.Scatter(
        x=positions,
        y=skew
    )

    data = [trace]

    pl.plot(data, filename='skew-graph')


# skew_plot("bacteria_1.fasta")

def nucl_content(fasta_file):
    nucleotides = {"A": 0, "T": 0, "G": 0, "C": 0}
    for record in SeqIO.parse(fasta_file, "fasta"):
        for s in range(0, len(record.seq)):
            nucleotides[record.seq[s]] += 1

    trace = go.Bar(
        x=["A", "T", "G", "C"],
        y=[nucleotides["A"], nucleotides["T"], nucleotides["G"], nucleotides["C"]]
    )

    data = [trace]
    pl.plot(data, filename='content-graph')


nucl_content("bacteria_1.fasta")
