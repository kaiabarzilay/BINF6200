"""
File: nt_fasta_stats.py

This program takes a fasta file and loops through it, organizing two lists.
One list contains the protein and ss data, and one the headers. This program
 then looks through the sequence list and outputs to a file statistics such as
 the number of A's, T's, G's, C's, and any N's, as well as the length of the
  sequence and also the %GC content of the entire sequence.

Sample command for executing the program:
$ python3 nt_fasta_stats.py

"""
import argparse
import sys


def main():  # pragma: no cover

    """Business Logic"""

    args = get_cli_args()
    fast_filename, outfile_name, character = args.fast_filename, args.outfile, args.character

    return fast_filename, outfile_name, character


def get_fasta_lists(fast_filename):

    """This function takes a fasta file and returns
    a list of sequences in the file and a list of
    headers to the sequence in the fasta file."""

    list_headers = []
    list_seqs = []

    with open(fast_filename, mode='r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                list_headers.append(line)
            else:
                list_seqs.append(line)
        if fast_filename.endswith(".fasta"):
            pass
        else:
            print("Did you provide a FASTA formatted file?")

    def _verify_lists(list_headers, list_seqs):

        """This function checks if the sizes of the lists
        are the same size. If they are not, exit."""

        length_headers = len(list_headers)
        length_seqs = len(list_seqs)
        if length_headers == length_seqs:
            pass
        else:
            print("Header and Sequence lists size are different in size")
            sys.exit()
    return _verify_lists(list_headers, list_seqs)


def print_sequence_stats(list_headers, outfile_name):

    """This function prints statistics of data files"""

    def _get_num_nucleotides(character, list_seqs):

        """This function makes sure that all characters in sequence are A, G, C, T or N"""
        character_letter = str(character)
        seq = str(list_seqs)
        for i in seq:
            if i != character_letter:
                print("Did not code this condition")
                sys.exit()

    header_string = str(list_headers)

    def _get_ncbi_accession(header_string):

        """This function returns the accession number for the data"""

        accession_string = header_string[1:10]
        return accession_string

    outfile_name.write(_get_ncbi_accession(header_string))

    with open(outfile_name, mode='w', encoding='utf-8') as output_file:
        output_file.write()


def get_cli_args():

    """This function uses argparse for arguments"""

    parser = argparse.ArgumentParser(
        description='Provide a FASTA file to generate nucleotide statistics')

    parser.add_argument('-i', '--infile',
                        dest='fast_filename',
                        help='Path to the file to open',
                        required=True)

    parser.add_argument('-o', '--outfile',
                        dest='outfile',
                        help='Path to the file to write tod',
                        required=True)

    parser.add_argument('-f', '--character',
                        dest='character',
                        help='character to find occurance of needed',)

    return parser.parse_args()


if __name__ == '__main__':  # pragma: no cover
    main()
