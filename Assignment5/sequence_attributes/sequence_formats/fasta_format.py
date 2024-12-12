"""Module of functions to implement"""

import sys
from typing import Tuple
from sequence_attributes.utils.io_utils import FileHandler


def get_fasta_lists(infile: str = None) -> Tuple[list, list]:

    """
    list, list: get_fasta_lists(fh_in)
    Takes : 1 arguments i.e. infile object. This functions opens the fh_in
    and splits the header and sequence into corresponding list and returns them.
    @param infile: A file for opening
    @return: Two list of headers, list of sequences
    """

    # create empty lists to store header and seq data
    header_list = []
    seq_list = []
    current_seq = ''  # always initialize variables in python.
    with FileHandler(infile, mode='r', encoding='utf-8') as fh_in:
        for line in fh_in:
            # matched a new record
            # check to see if line is header
            if line[0] == ">":
                header_list.append(line[1:].replace('\n', '').replace('\r', ''))
                if current_seq != '':
                    seq_list.append(current_seq)  # add on the data if there was sequence data
                current_seq = ''  # reset the variable
            else:
                current_seq += line.replace('\n', '').replace('\r', '')

    if current_seq:
        seq_list.append(current_seq)

    # were the lists the same size?
    _verify_lists(header_list=header_list, seq_list=seq_list)

    return header_list, seq_list


def _verify_lists(header_list: list = None, seq_list: list = None) -> bool:
    """
    True : _verify_lists(header_list, seq_list)
    Takes : 2 arguments i.e. Header list and Seq list. Returns nothing if the
    size of the two lists are same and exists otherwise.
    @param header_list: List of headers for the fasta fh_in
    @param seq_list: List of sequences for the fasta fh_in
    @return: Boolean, True or exists the program
    """
    # check size of both the header and seq list
    size1 = len(header_list)
    size2 = len(seq_list)
    # if the sizes of both lists are the same pass, else exit
    if size1 != size2:
        sys.exit("Header and Sequence lists are different in size\n" +
                 "Did you provide a FASTA formatted fh_in")
    else:
        return True
