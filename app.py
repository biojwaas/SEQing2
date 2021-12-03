# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_bio
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash import dcc
from dash import html

# Static Default style
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
from flask import send_from_directory

app = dash.Dash(__name__)#, external_stylesheets=external_stylesheets)


# This method provides the options for SEQing2
def dropdown():
    item = [{'label': 'IClip', 'value': 'NULL'},
            {'label': 'RNA-Seq', 'value': 'NULL'},
            {'label': 'Settings', 'value': 'NULL'}]
    return html.Div([
        dbc.InputGroup([
            dcc.Dropdown(id="Gene-Selection", placeholder="Gene-Selection..."),
            dcc.Dropdown(id='Select-Menu', options=item,
                         placeholder="Menu",
                         style=dict(width='40%', display='inline-block', verticalAlign='middle'))
        ])
    ])


HOSTED_GENOME_DICT = [
    {'value': 'tair', 'label': 'A.Thaliana'},
    {'value': 'covid19', 'label': 'Sars-CoV-2 (ASM985889v3)'},
    {'value': 'bedGenes', 'label': 'Test-BedGrpah'},
]


def clustergram():
    return html.Div([
        dcc.Loading(id='default-igv-container'),
        html.Hr(),
        html.P('Select the genome to display below.'),
        dcc.Dropdown(
            id='default-igv-genome-select',
            options=HOSTED_GENOME_DICT,
            value='covid19'
        )
    ])


app.layout = clustergram()

# Starts the server, which make a file to an url
@app.server.route('/samples/<path:path>')
def send_fa(path):
    response = send_from_directory('samples/', path)
    return response


# Return the IGV component with the selected genome.
@app.callback(
    Output('default-igv-container', 'children'),
    Input('default-igv-genome-select', 'value')
)
def return_igv(genome):
    reference = {
        'id': 'ASM985889v3',
        'name': 'Sars-CoV-2 (ASM985889v3)',
        'fastaURL': 'https://s3.amazonaws.com/igv.org.genomes/covid_ASM985889v3/GCF_009858895.2_ASM985889v3_genomic.fna',
        'indexURL': 'https://s3.amazonaws.com/igv.org.genomes/covid_ASM985889v3/GCF_009858895.2_ASM985889v3_genomic.fna.fai',
        'order': 1000000,
        'tracks': [
            {
                'name': 'Annotations',
                'url': 'https://s3.amazonaws.com/igv.org.genomes/covid_ASM985889v3/GCF_009858895.2_ASM985889v3_genomic.gff.gz',
                'displayMode': 'EXPANDED',
                'nameField': 'gene',
                'height': 150,
                'color': 'rgb(176,141,87)'
            }
        ]
    }
    thaliana = {
        #"id": "tair",
        "name": "A. thaliana (TAIR 10)",
        'sourceType': "file",
        "url": "http://localhost:8012/TAIR10_chr_all_noYWMKSRD.fa",
        "tracks": [
            {
                "name": "Genes",
                "type": "annotation",
                "format": "gtf",
                "sourceType": "file",
                "url": "http://localhost:8012/Araport11_protein_coding.201606.gtf.gz",
            }
        ]
    }
    bedgraph = {
        # 'id':'bedGenes',
        'name': "Annotation",
        'type': "annotation",
        'format': "bed",
        'sourceType': "file",
        'url': "http://localhost:8012/7GFPLL24-2016_bsite.bed",
        'displayMode': "EXPANDED"
    }

    if genome == 'tair':
        return html.Div([
            dash_bio.Igv(
                id='reference-igv',
                tracks=[
                    {'name': 'tair',
                     'url': 'samples/Arabidopsis_thaliana.TAIR10.dna.toplevel.fa'
                     }]
            )
        ])

    if genome == 'covid19':
        return html.Div([
            dash_bio.Igv(
                id="reference-igv",
                reference = reference
            )
        ])

    if genome == 'bedGenes':
        return html.Div([
            dash_bio.Igv(
                id='reference-igv',
                tracks=[
                    {'name': 'bedGenes',
                     'url': 'Araport11_protein_coding.201606.bed'
                     }]
            )
        ])


if __name__ == '__main__':
    app.run_server(debug=True)
    # InitialiseServer.run_http_server(8012)
