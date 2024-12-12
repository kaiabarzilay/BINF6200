"""
This program finds all gene symbols that appear both
in the chr21_genes.txt file and in the HUGO_genes.txt
file. These gene symbols are then  printed to a file
in alphabetical order. This program calls functions
from assignment4_utils.py module.

Sample command for executing the program:
$ python3 intersection_of_gene_names.py
 -i1 chr21_genes.txt -i2 HUGO_genes.txt
"""

import argparse
from assignment4.io_utils import mkdir_from_infile
from assignment4.assignment4_utils import (create_list1, create_list2,
                                           name_intersection,
                                           name_difference_data1,
                                           name_difference_data2)


def main():  # pragma no cover

    """Business Logic"""

    args = get_cli_args()
    gene_list1 = args.input_file1
    gene_list2 = args.input_file2
    output_filename = 'OUTPUT/intersection_output.txt'
    mkdir_from_infile(output_filename)
    column_data1 = set(create_list1(gene_list1))
    column_data2 = set(create_list2(gene_list2))
    shared_names = name_intersection(column_data1, column_data2)
    common_names = len(shared_names)
    unique_data1 = name_difference_data1(column_data1, column_data2)
    unique_data2 = name_difference_data2(column_data2, column_data1)

    print_output(shared_names, common_names, unique_data1,
                 unique_data2, output_filename)


def print_output(shared_names, common_names, unique_data1,
                 unique_data2, output_filename):

    """This function prints the intersections and prints to file"""

    for value in shared_names:
        output_filename.write(value).sorted()

    print("Number of unique gene names in hgnc_complete_set_reduced.txt:",
          unique_data1)
    print("Number of unique gene names in HUGO_genes.txt:", unique_data2)
    print("Number of common gene symbols found:", common_names)
    print("Output stored in OUTPUT/intersection_output.txt")


def get_cli_args():  # pragma no cover

    """This function uses argparse for arguments"""

    parser = argparse.ArgumentParser(
        description='Provide two gene list (ignore header line),'
                    ' find intersection')

    parser.add_argument('-i1 INFILE1', '--infile1 INFILE1',
                        dest='input_file1',
                        help='Gene list 1 to open')

    parser.add_argument('-i2 INFILE2', '--infile2 INFILE2',
                        dest='input_file2',
                        help='Gene list 2 to open')

    return parser.parse_args()


if __name__ == "__main__":
    main()
