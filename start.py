#!/usr/bin/env python
# -*- coding: utf-8 -*-

from components import iclip
import files.FilesHandler
from files import ARGS
import runpy

data_set_names = []
bs_raw_dfs = {}
gene_annotations = []  # Is missing. Is needs loadAnnotations


def __check_args(args):
    if args.has_option('dir'):
        handler = files.FilesHandler.FileHandler(args.get_directory())
        iclip.IClipHandler(handler)
    # TODO: further argument check


if __name__ == '__main__':
    """Start the application via console"""
    # TODO: Maybe should be directly in the class ARGS
    args = ARGS.Args()
    __check_args(args)
    globalDict = {
        'data_set_names': data_set_names,  # Names for the data sets
        'bs_raw_dfs': bs_raw_dfs,  # Dataframes with iCLIP data
    }
    # app = dash.Dash(__name__)
    # app.run_server(debug=True)
    runpy.run_module('app', init_globals=globalDict, run_name='__main__')
