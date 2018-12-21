#!/usr/bin/python
import dash
import dash_core_components as dcc
import dash_html_components as html
from Bio import SeqIO
from dash.dependencies import Input, Output
import plotly.graph_objs as go

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
    nucleotides = {"A": 0, "T": 0, "G": 0, "C": 0}
    for record in SeqIO.parse(fasta_file, "fasta"):
        for s in range(0, len(record.seq)):
            nucleotides[record.seq[s]] += 1

    x = ["A", "T", "G", "C"]

    y = [nucleotides["A"], nucleotides["T"], nucleotides["G"], nucleotides["C"]]

    return [x, y]


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div([
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
                {'label': 'Nucleotide Content', 'value': 'NC'}
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
                margin={'l': 50, 'b': 40, 't': 10, 'r': 10}
            )
        }
    else:
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
                    title=input_value,
                    xaxis={'title': 'Nucleotide Position'},
                    yaxis={'title': 'Skew'},
                    margin={'l': 40, 'b': 40, 't': 40, 'r': 10}
                )
            }
        else:
            return {
                'data': [
                    go.Bar(
                        x=nucl_content(input_value)[0],
                        y=nucl_content(input_value)[1],
                        opacity=0.7,
                    )
                ],
                'layout': go.Layout(
                    title=input_value,
                    xaxis={'title': 'Nucleotide'},
                    yaxis={'title': 'Amount'},
                    margin={'l': 40, 'b': 40, 't': 40, 'r': 10}
                )
            }


if __name__ == '__main__':
    app.run_server(debug=True)

