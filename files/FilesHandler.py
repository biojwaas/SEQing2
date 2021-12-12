import os

from os import listdir
from os.path import isfile, join
from collections import deque

from files import File_type
from files.File import FileInput
from files.FileHandlerInterface import FileHandlerInterface


class FileHandler(FileHandlerInterface):

    def __init__(self, path):
        self.fasta_files = deque()
        self.bed_files = deque()
        self.bedgraph_files = deque()
        self.gtf_files = deque()
        self.gff_files = deque()
        self.path_of_files = path
        self.SERVER_FOLDER = 'tracks/'
        self.load_all_files(path)

    def get_fastas(self):
        """Get all fasta files, which are stored
        @:return fasta files"""
        return self.fasta_files

    def get_gtfs(self):
        """Get all gtf files, which are stored
        @:return gtf files"""
        return self.gtf_files

    def get_beds(self):
        """Get all bed files, which are stored
        @:return bed files"""
        return self.bed_files

    def get_beds_as_dicts(self):
        return [{'value': bed.get_filename(), 'label': bed.get_filename()} for bed in self.get_beds()]

    def get_bedgraphs(self):
        """Get all bedgraph files, which are stored
        @:return bedgraph files"""
        return self.bedgraph_files

    def get_gffs(self):
        """Get all gff files, which are stored
        @:return gff files"""
        return self.gff_files

    def get_specific_file(self, file):
        # at the moment just for bed
        for entry in self.bed_files:
            if entry.get_filename() == file:
                return entry
        return FileNotFoundError

    def load_all_files(self, path):
        """Load all Files into the files handler"""
        only_files = [f for f in listdir(path) if isfile(join(path, f))]
        for file in only_files:
            # print(os.access(file, os.EX_OK)) does not work
            try:
                split_up = os.path.splitext(file)
                # file_name = split_up[0]
                file_extension = split_up[1]
                if file_extension == '.fa':
                    fasta_file = FileInput(file.__str__(), self.path_of_files / file.__str__(),
                                           File_type.Filetype.FASTA,
                                           False, False, False, self.SERVER_FOLDER + file.__str__())
                    self.fasta_files.append(fasta_file)
                if file_extension == '.bed':
                    bed_file = FileInput(file.__str__(), self.path_of_files / file.__str__(),
                                         File_type.Filetype.BED,
                                         False, False, False, self.SERVER_FOLDER + file.__str__())
                    self.bed_files.append(bed_file)
                if file_extension == '.bedgraph':
                    bedgraph_file = FileInput(file.__str__(), self.path_of_files / file.__str__(),
                                              File_type.Filetype.BEDGRAPH,
                                              False, False, False, self.SERVER_FOLDER + file.__str__())
                    self.bedgraph_files.append(bedgraph_file)
                if file_extension == '.gtf':
                    gtf_file = FileInput(file.__str__(), self.path_of_files / file.__str__(),
                                         File_type.Filetype.GTF,
                                         False, False, False, self.SERVER_FOLDER + file.__str__())
                    self.gtf_files.append(gtf_file)
                if file_extension == '.gff':
                    gff_file = FileInput(file.__str__(), self.path_of_files / file.__str__(),
                                         File_type.Filetype.GTF,
                                         False, False, False, self.SERVER_FOLDER + file.__str__())
                    self.gff_files.append(gff_file)
            # TODO: Add zip files and handle the files better than just by file_extension to identify the file type
            except PermissionError:
                raise OSError
