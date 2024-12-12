"""
This program counts how many genes are in each category (1.1, 1.2, 2.1 etc.)
based on data from the chr21_genes.txt file. The program then prints
the results so that categories are arranged in ascending order to an
output file. This program calls functions from assignment4_utils.py
module.

Sample command for executing the program:
$ python3 find_common_cats.py # runs by default
"""

import argparse
from assignment4.io_utils import mkdir_from_infile
from assignment4.assignment4_utils import (create_dictionary_1,
                                           create_dictionary_2, category_count)


def main():  # pragma no cover

    """Business Logic"""

    args = get_cli_args()
    input_file1 = args.input_file1
    input_file2 = args.input_file2
    output_filename = 'OUTPUT/categories.txt'
    mkdir_from_infile(output_filename)

    gene_dict1 = sorted(create_dictionary_1(input_file1))
    gene_dict2 = sorted(create_dictionary_2(input_file2))
    gene_count_final = category_count(gene_dict1)

    print_output(gene_count_final, gene_dict2, output_filename)


def print_output(category_count_final, gene_dict2, output_filename):

    """This function prints the category, description and occurrence"""

    with open(output_filename, 'w', encoding="utf-8") as output_file:
        for key, value_pair in gene_dict2:
            output_file.write(f"{key}" + f"{category_count_final}" +
                              f"{value_pair}")


def get_cli_args():  # pragma no cover

    """This function uses argparse for arguments"""

    parser = argparse.ArgumentParser(
        description='Combine on gene name and count the category occurrence')

    parser.add_argument('-i1 INFILE1', '--infile1 INFILE1',
                        dest='input_file1',
                        help='Path to the gene description fh_in to open')

    parser.add_argument('-i2 INFILE2', '--infile2 INFILE2',
                        dest='input_file2',
                        help='Path to the gene category to open')

    return parser.parse_args()


if __name__ == "__main__":
    main()
