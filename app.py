#!/usr/bin/python
import dash
import dash_core_components as dcc
import dash_html_components as html
from Bio import SeqIO
from Bio.SeqUtils import GC
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import os

# Ideas: Allow for database queries as input (http://biopython.org/DIST/docs/tutorial/Tutorial.html#chapter:entrez)
# Allow for multiple files and graphs to be open in one window
# Look into new graphs


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

    return [positions, skew]


def nucl_content(fasta_file):
    nucleotides = {"A": 0, "T": 0, "G": 0, "C": 0, "N": 0}
    for record in SeqIO.parse(fasta_file, "fasta"):
        for s in range(0, len(record.seq)):
            nucleotides[record.seq[s]] += 1

    x = ["A", "T", "G", "C", "N"]

    y = [nucleotides["A"], nucleotides["T"], nucleotides["G"], nucleotides["C"], nucleotides["N"]]

    return [x, y]


def gc_content(fasta_file):
    y = sorted(GC(record.seq) for record in SeqIO.parse(fasta_file, "fasta"))
    x = [i for i in range(1, len(y)+1)]

    return [x, y]


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': '#cceeff'}, children=[
    html.H1(
        children="FASTA Dash"
    ),
    html.Div([
        dcc.Upload(id="input-file",
                    children=html.Div([
                        'Drag and Drop or ',
                        html.A('Select Files')
                    ])
         ),
        dcc.RadioItems(id="graph-type",
            options=[
                {'label': 'Skew Plot', 'value': 'SP'},
                {'label': 'Nucleotide Content', 'value': 'NC'},
                {'label': 'GC%', 'value': 'GC'}
            ],
            value='SP',
            labelStyle={'display': 'inline-block'}
        )
    ]),


    dcc.Graph(
        id='graph',
    )
])


@app.callback(
    Output(component_id='graph', component_property='figure'),
    [Input(component_id='input-file', component_property='filename'),
     Input(component_id='graph-type', component_property='value')]
)
def update_div(input_value, graph_type):
    if not input_value:
        return {
            'data': [
                go.Scatter(
                    x=[0],
                    y=[0],
                    opacity=0.7,
                )
            ],
            'layout': go.Layout(
                xaxis={'title': 'Nucleotide Position'},
                yaxis={'title': 'Skew'},
                margin={'l': 70, 'b': 10, 't': 10, 'r': 10}
            )
        }
    else:
        input_value = os.path.join("Input_Files", input_value)
        if graph_type == "SP":
            return {
                'data': [
                    go.Scatter(
                        x=skew_plot(input_value)[0],
                        y=skew_plot(input_value)[1],
                        opacity=0.7,
                    )
                ],
                'layout': go.Layout(
                    title=input_value.split("\\")[-1],
                    xaxis={'title': 'Nucleotide Position'},
                    yaxis={'title': 'Skew'},
                    margin={'l': 40, 'b': 40, 't': 40, 'r': 10}
                )
            }
        elif graph_type == "NC":
            return {
                'data': [
                    go.Bar(
                        x=nucl_content(input_value)[0],
                        y=nucl_content(input_value)[1],
                        opacity=0.7,
                    )
                ],
                'layout': go.Layout(
                    title=input_value.split("\\")[-1],
                    xaxis={'title': 'Nucleotide'},
                    yaxis={'title': 'Amount'},
                    margin={'l': 40, 'b': 40, 't': 40, 'r': 10}
                )
            }
        elif graph_type == "GC":
            return {
                'data': [
                    go.Scatter(
                        x=gc_content(input_value)[0],
                        y=gc_content(input_value)[1],
                        opacity=0.7,
                    )
                ],
                'layout': go.Layout(
                    title=input_value.split("\\")[-1],
                    xaxis={'title': 'Genes'},
                    yaxis={'title': 'GC%'},
                    margin={'l': 40, 'b': 40, 't': 40, 'r': 10}
                )
            }


if __name__ == '__main__':
    app.run_server(debug=True)

