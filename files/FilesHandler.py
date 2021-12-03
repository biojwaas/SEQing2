import os
import pathlib
from os import listdir
from os.path import isfile, join
from collections import deque

from files import File_type
from files.File import FileInput
from files.FileHandlerInterface import FileHandlerInterface


class FileHandler(FileHandlerInterface):

    def __init__(self, path):
        self.fasta_files = deque()
        self.path_of_files = path
        self.load_all_files(path)

    def get_fastas(self):
        """Get all fasta files, which are stored
        @:return fasta files"""
        return self.fasta_files

    def get_gtfs(self):
        pass

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
                    fastafile = FileInput(self.path_of_files / file.__str__(),
                                          File_type.Filetype.FASTA,
                                          False, False, False)
                    self.fasta_files.append(fastafile)
            except PermissionError:
                raise OSError
        # TODO: Other filetypes should be added
