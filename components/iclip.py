#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from files.File_type import Filetype

fastadict = {}


class IClipHandler:

    def __init__(self, files_handler):
        self.handler = files_handler
        self.dummy_file_bedgraph = files_handler.get_bedgraphs()[0]
        self.dummy_file_fasta = files_handler.get_fastas()[0]
        self.dummy_file_gff = files_handler.get_gffs()[0]
        self.dummy_file_bed = files_handler.get_beds()[0]
        self.current_file = files_handler.get_beds()[0]

    def set_item_dict(self, filetype):
        if filetype == Filetype.BEDGRAPH:
            return self.dummy_file_bedgraph.get_general_dict()
        if filetype == Filetype.BED:
            return self.dummy_file_bed.get_general_dict()

    # TODO: Need to get more dicts not just the first one

    def set_reference(self):
        return self.current_file.get_general_dict()

    def set_item_gff_dict(self):
        return self.dummy_file_gff.get_general_dict()

    def set_gene_selection(self):
        return self.dummy_file_fasta.get_dict()

    def set_selected_file(self, file):
        # current only bed-file
        self.current_file = self.handler.get_specific_file(file)

    def get_current_gene_dict(self):
        return self.current_file.get_dict()

    def get_current_file(self):
        return self.current_file

    def get_locus(self, genome):
        return self.dummy_file_bed.get_locus(genome)

    def get_file_options(self):
        return [{'value': bed.get_filename(), 'label': bed.get_filename()} for bed in self.handler.get_beds()]
