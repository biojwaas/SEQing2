# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_bio
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash import dcc
from dash import html

# Static Default style
app = dash.Dash(__name__)


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
    {'value': 'tair10', 'label': 'A.Thaliana'},
    {'value': 'covid19', 'label': 'Sars-CoV-2 (ASM985889v3)'},
    {'value': 'test', 'label':'Test-BedGrpah'},
]


def clustergram():
    return html.Div([
        dcc.Loading(id='default-igv-container'),
        html.Hr(),
        html.P('Select the genome to display below.'),
        dcc.Dropdown(
            id='default-igv-genome-select',
            options=HOSTED_GENOME_DICT,
            value='tair10'
        )
    ])


# tair10

app.layout = clustergram()


# Return the IGV component with the selected genome.
@app.callback(
    Output('default-igv-container', 'children'),
    Input('default-igv-genome-select', 'value')
)
def return_igv(genome):
    track = {
        'id': 'Arabidopsis_thaliana',
        'name': 'Arabidopsis Thaliana',
        # 'type': 'annotation',
        # 'format': "fa",
        #'sourceType': "file",
        'fastaURL': 'http://ftp.ensemblgenomes.org/pub/plants/release-51/fasta/arabidopsis_thaliana/dna_index/Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.gz ',
        #'url' 'samples/TAIR10_chr_all_noYWMKSRD.fa'
        'indexURL': 'http://ftp.ensemblgenomes.org/pub/plants/release-51/fasta/arabidopsis_thaliana/dna_index/Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.gz.fai',
        'order': 1000000,
        'tracks': [{
            'name': 'Annotations',
            'format': 'gtf',
            'url': 'samples/Araport11_protein_coding.201606.gtf',
            'displayMode': 'EXPANDED',
            'nameField': 'gene',
            'height': 150,
            'color': 'rgb(176,141,87)'
        }]
    }
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

    bedgraph = {
      'name': "Genes",
      'type': "annotation",
      'format': "bed",
      'sourceType': "file",
      'url': "//igv.broadinstitute.org/annotations/hg19/genes/gencode.v18.collapsed.bed",
      'indexURL': "//igv.broadinstitute.org/annotations/hg19/genes/gencode.v18.collapsed.bed.idx",
      'displayMode': "EXPANDED"
    }

    if genome == 'tair10':
        return html.Div([
            dash_bio.Igv(
                id='reference-igv',
                reference=track,
            )
        ])
    if genome == 'covid19':
        return html.Div([
            dash_bio.Igv(
                id='reference-igv',
                reference=reference,
            )
        ])
    if genome =='test':
        return html.Div([
            dash_bio.Igv(
                id = 'reference-igv',
                genome= bedgraph,
            )
        ])


if __name__ == '__main__':
    app.run_server(debug=True)
