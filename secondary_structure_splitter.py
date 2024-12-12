"""
File: secondary_structure_splitter.py

This program takes a fasta file and loops through it, organizing two lists.
One list contains the protein and ss data, and one the headers. This program
 then looks through these two lists and outputs the protein sequence and headers
 to a file called pdb_protein.fasta, and the secondary structure sequence and
 headers to a file called pdb_ss.fasta.

Sample command for executing the program:
$ python secondary_structure_splitter.py  --infile ss.txt

"""
import argparse
import sys


def main():  # pragma: no cover

    """Business Logic"""

    args = get_cli_args()
    fast_filename = args.fast_filename
    pdb_protein = "/Assignment3/pdb_protein.fasta"
    pdb_ss = "/Assignment3/pdb_ss.fasta"

    return fast_filename, pdb_protein, pdb_ss


def get_fasta_lists(fast_filename):

    """This function takes a fasta file and returns
    a list of sequences in the file and a list of
    headers to the sequence in the fasta file."""

    list_headers = []
    list_seqs = []

    with open(fast_filename, mode='r', encoding='utf-8') as file:
        for line in file:
            line = line.rstrip()
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

        if length_headers != length_seqs:
            print("Header and Sequence lists size are different in size", '\n',
                  "Did you provide a fasta formatted file?")
            sys.exit()

    return _verify_lists(list_headers, list_seqs)


def output_results_to_files(list_headers,
                            list_seqs, pdb_protein, pdb_ss):

    """This function prints out two files for protein
     and sequences for the fasta file"""

    with open(pdb_protein, 'w', encoding="utf-8"), open(pdb_ss, 'w', encoding="utf-8"):
        protein_count = 0
        ss_count = 0
        for header_line, seq_line in list_headers, list_seqs:
            if header_line.endswith(":secstr"):
                pdb_ss.write(header_line)
            else:
                pdb_protein.write(header_line)
            if seq_line in seq_line.startswith(" "):
                pdb_ss.write(seq_line)
                ss_count += 1
            else:
                pdb_protein.write(seq_line)
                protein_count += 1

    print("Found", protein_count, "protein sequences", "\n",
          "Found", ss_count, "ss sequences", file=sys.stderr)


def get_cli_args():  # pragma: no cover

    """This function uses argparse for arguments"""

    parser = argparse.ArgumentParser(
        description='Provide a FASTA file to perform'
                    ' splitting on sequence and secondary structure')

    parser.add_argument('-i', '--infile',
                        dest='fast_filename',
                        help='Path to file to open',
                        required=True)

    return parser.parse_args()


if __name__ == '__main__':  # pragma: no cover
    main()
