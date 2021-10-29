# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import datetime

import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html

# import plotly.express as px
# import pandas as pd
# Static Default style
tabStyle = {'padding': '0', 'line-hight': '5vh'}
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


def input_bedfile():
    return html.Div([
        dcc.Upload(
            id='Upload-BED',
            children=html.Div([
                'Drag and Drop or ', html.A('Select Files')
            ]),
            style={
                'width': '100%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '10px'
            },
            # Allow multiple files to be uploaded
            multiple=True
        ),
        html.Div(id='output-BED-upload')
    ])


# Sollte vielleicht in ein eigenes Modul gepackt werden
def parse_contents(contents, filename, date):
    return html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),

        # Try to accept BED-file format
        html.Data(src=contents),
        html.Hr(),
        html.Div('Raw-Content'),
        html.Pre(contents[0:200] + '...', style={'whiteSpace': 'pre-wrap', 'wordBreak': 'break-all'})
    ])


app.layout = html.Div(children=[
    html.H1(children='SEQing2'),  # kann entfernt werden

    html.Div(children=[
        html.H1(id='headline', children='Report')
    ],
        style={'width': '90vw', 'display': 'table-cell', 'verticalalign': 'middle'}
    ),
    html.Div(
        children=[
            dropdown(),
            input_bedfile()
        ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
