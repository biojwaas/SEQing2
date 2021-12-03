#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Bio import SeqIO

from files.File_type import Filetype


class FileInput:
    """Decorator for file checking
    @:param file Path
    @:param file Type (gtf,bed,fa,bedgraph)
    @:param file is zipped or not(True or False)
    @:param type of zip if zipped(gz)
    @:param header is present (True or False)"""

    def __init__(self, file_path, file_type, zipped, zip_type, header_present):
        self.file_path = file_path
        self.file_type = file_type
        self.zipped = zipped
        self.zip_type = zip_type
        self.header_present = header_present

    def get_dict(self):
        """Method returns a dictionary of the file
        @:return dict"""
        if self.file_type == Filetype.FASTA:
            return {rec.id: rec.seq for rec in SeqIO.parse(self.file_path, "fasta")}
        # TODO: Return a dictionary of GTF, BED, BEDGRAPH

    def get_path(self):
        """Get the absolut path from the File
        @:return the location File"""
        return self.file_path


    """def check_input_file(file_path):
        #A function to test an input file and classifies it by content
        # try to guess file type by analysing the head
        guessed_type = ft.guess(file_path)
        file_zipped = False

        if guessed_type is None:
            # read uncompressed head
            file_head = pd.read_csv(file_path, sep='\t', header=None, nrows=5, error_bad_lines=False)
            zip_type = None
        elif guessed_type.mime in ['application/gzip', 'application/x-bzip2', 'application/zip']:
            zip_type = guessed_type.mime.split('/')[1]
            # read compressed head
            file_head = pd.read_csv(file_path, compression='infer', sep='\t', header=None, nrows=5,
                                    error_bad_lines=False, warn_bad_lines=False)
            file_zipped = True
        else:
            # return unsupported file type
            return FileInput(file_path, 'unsupported', False, False)
            # zip_type == None
        head_dtypes = np.array(file_head.dtypes)
        # check for header (no numbers in first row)
        header_present = not any(cell == np.int for cell in head_dtypes)
        header = pd.Series()
        if header_present:
            header = file_head.iloc[0]
            if file_zipped:
                file_head = pd.read_csv(file_path, compression='infer', sep='\t', header=None, nrows=5, skiprows=1,
                                        comment='#')
            else:
                file_head = pd.read_csv(file_path, sep='\t', header=None, nrows=5, skiprows=1, comment='#')

        # assign file type by shape of table
        head_dim = file_head.shape
        # check for BED4
        if head_dim[1] == 4:
            return FileInput(file_path, 'BED4', file_zipped, zip_type, header_present)
        # check for BED6
        elif head_dim[1] == 6:
            return FileInput(file_path, 'BED4', file_zipped, zip_type, header_present)
        # check for GFF or GTF
        elif head_dim[1] == 9:
            if not header.empty:
                for col in header:
                    if 'gff-version 3' in col:
                        return FileInput(file_path, 'GFF3', file_zipped, zip_type, header_present)
                    else:
                        return FileInput(file_path, 'GTF', file_zipped, zip_type, header_present)
            else:
                if '"' in file_head.iloc[0, 8]:
                    return FileInput(file_path, 'GTF', file_zipped, zip_type, header_present)
        elif head_dim[1] == 12:
            return FileInput(file_path, 'BED12', file_zipped, zip_type, header_present)
        else:
            # unsupported format
            return FileInput(file_path, 'unsupported', False, zip_type, header_present)

    # There might be some Packages that allow access to the file. This has not be
    # written by myself
    def getGTFFIle(self):
        gff3_dir = self.file_path()
        GFF3 = pd.read_csv(
            filepath_or_buffer=gff3_dir + "/samples/Araport11_protein_coding.201606.gtf",
            sep='\t',
            header=None,
            names=['chrom', 'chromStart', 'chromEnd', 'geneID', 'transID', 'score', 'strand', 'thickStart',
                   'thickEnd', 'itemRGB', 'blockCount', 'blockSizes', 'blockStarts'],
            skiprows=[i for i in xrange(25)]
        )
        GFF3 = GFF3[GFF3['source'].notnull()]
        return GFF3"""