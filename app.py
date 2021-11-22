# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import io
import os
import pathlib

import dash
import dash_bio
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash import dcc
from dash import html
from igv_reports import tracks
from igv_reports.feature import FeatureReader, _NonIndexed, parse_gff, parse_bed
from pprint import pprint as pp

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
            value='tair10'
        )
    ])

app.layout = clustergram()


# Return the IGV component with the selected genome.
@app.callback(
    Output('default-igv-container', 'children'),
    Input('default-igv-genome-select', 'value')
)
def return_igv(genome):
    fastaFile = pathlib.Path(__file__).parent/'samples/Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.gz'
    indexFile = pathlib.Path(__file__).parent/'samples/Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.gz.fai'


    data = tracks.get_name('samples/TAIR10_GFF3_genes.gff')
    gff_file = pathlib.Path(__file__).parent/'samples/TAIR10_GFF3_genes.gff'
    ''' gff_path = str(gff_file.resolve())
    pp(gff_file.exists()) # 1 True
    pp(gff_file.is_file()) #2 True
    pp(os.access(gff_path, os.R_OK)) #3 True
    pp(gff_file.is_absolute()) #4 True
    feature_file = FeatureReader(gff_path)
    nonIndex_file = _NonIndexed(gff_path)
    content = feature_file.slice()
    features = parse_gff(io.StringIO(content))
    noIndex_features = parse_gff(io.StringIO(nonIndex_file.slice()))'''

    '''track = {
        #'id': 'Arabidopsis_thaliana',
        'id':'tair10',
        'name': 'Arabidopsis Thaliana',
        # 'type': 'annotation',
        # 'format': "fa",
        'sourceType': "file",
        #'fastaURL': 'http://ftp.ensemblgenomes.org/pub/plants/release-51/fasta/arabidopsis_thaliana/dna_index/Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.gz',
        #'fastaURL':fastaFile,
        #'fastaURL':'samples/Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.gz',
        #'url' 'samples/TAIR10_chr_all_noYWMKSRD.fa'
        'url':'samples/Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.gz',

        #'indexURL': 'http://ftp.ensemblgenomes.org/pub/plants/release-51/fasta/arabidopsis_thaliana/dna_index/Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.gz.fai',
        #'url':'samples/Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.gz.fai',
        #'indexURL: indexFile,
        #'indexURL':'samples/Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.gz.fai',
        #'order': 1000000,
        'tracks': [{
            'name': 'Annotations',
            'type': 'annotation',
            #'format': 'gtf',
            #'url': 'samples/try1.gtf',
            'format': 'gff3',
            'sourceType': 'file',
            #'url': 'https://s3.amazonaws.com/igv.org.genomes/tair10/TAIR10_GFF3_genes.gff',
            #'url': '\\\wsl.localhost\\Ubuntu-20.04\\home\\jonas\\Coding\\PycharmProjects\\Abschlussprojekt\\SEQing2\\samples\\TAIR10_GFF3_genes.gff',
            #'url' : gff_path,
            'url':'samples/TAIR10_GFF3_genes.gff',
            'displayMode': 'EXPANDED',
            #'nameField': 'gene',
            #'height': 150,
            #'color': 'rgb(176,141,87)'
        }]
    }'''
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
        "id": "tair10",
        "name": "A. thaliana (TAIR 10)",
        'sourceType': "file",
        #"fastaURL": "https://s3.amazonaws.com/igv.org.genomes/tair10/TAIR10_chr_all.fas",
        "url": "samples/TAIR10_chr_all_noYWMKSRD.fa",
        #"indexURL": "https://s3.amazonaws.com/igv.org.genomes/tair10/TAIR10_chr_all.fas.fai",
        #"aliasURL": "https://s3.amazonaws.com/igv.org.genomes/tair10/TAIR10_alias.tab",
        #"order": 1000000,
        "tracks": [
            {
                "name": "Genes",
                "type":"annotation",
                "format": "gtf",
                "sourceType":"file",
                "url": "samples/Araport11_protein_coding.201606.gtf.gz",

                #"url": 'samples/Araport11_protein_coding.201606.gtf',
                #"url": 'samples/Araport11_protein_coding.201606.bed',
                #"url":"samples/7GFPLL24-2016_bsite.bedgraph",
                #"indexed": "samples/foo.bed.gz.tbi",
                #"removable": 'false',

            }
        ]
    }
    bedgraph = {
        #'id':'bedGenes',
        'name': "Annotation",
        'type': "annotation",
        'format': "bed",
        'sourceType': "file",
        'url': "samples/Araport11_protein_coding.201606.bed",
        #'indexURL': "//igv.broadinstitute.org/annotations/hg19/genes/gencode.v18.collapsed.bed.idx",
        'displayMode': "EXPANDED"
    }

    if genome == 'tair10':
        return html.Div([
            dash_bio.Igv(
                id='reference-igv',
                reference=thaliana,
            )
        ])

    if genome == 'covid19':
        return html.Div([
            dash_bio.Igv(
                id="reference-igv",
                reference=reference,
            )
        ])

    if genome == 'bedGenes':
        return html.Div([
            dash_bio.Igv(
                id='reference-igv',
                reference=bedgraph,
            )
        ])


if __name__ == '__main__':
    app.run_server(debug=True)
