#!/usr/bin/python
from Bio import SeqIO
import plotly.plotly as pl
import plotly.graph_objs as go

skew = [0]
positions = []

for record in SeqIO.parse("bacteria_1.fasta", "fasta"):
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

