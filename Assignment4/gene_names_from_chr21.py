"""
This program asks the user to enter a gene symbol and then prints the
description for that gene based on data from the chr21_genes.txt file.
This program calls functions from assignment4_utils.py module.

Sample command for executing the program:
$ python3 gene_names_from_chr21.py -i chr21_genes.txt

"""

import argparse
import sys
from assignment4.assignment4_utils import create_dictionary


def main():  # pragma no cover

    """Business Logic"""

    args = get_cli_args()
    input_file = args.input_file
    gene_name = input("Enter gene name of interest. Type quit to exit:")

    gene_dictionary = create_dictionary(input_file)

    if gene_name in ('quit', 'exit'):
        print("Thanks for querying the data.")
        sys.exit()

    print_output(gene_dictionary, gene_name)


def print_output(gene_dictionary, gene_name):

    """This function prints the output description"""
    if gene_name in gene_dictionary:
        print(gene_name, "found! Here is the description:", "\n",
              gene_dictionary[gene_name])
    else:
        print("Not a valid gene name.")
        print(gene_dictionary)


def get_cli_args():  # pragma no cover

    """This function uses argparse for arguments"""

    parser = argparse.ArgumentParser(
        description='Open chr21_genes.txt, and ask user for a gene name')

    parser.add_argument('-i INFILE', '--infile INFILE',
                        dest='input_file',
                        help='Path to the fh_in to open')

    return parser.parse_args()


if __name__ == "__main__":
    main()
