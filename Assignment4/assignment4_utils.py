"""
Modules implemented for programs:
gene_names_from_chr21.py
find_common_cats.py
intersection_of_gene_names.py
"""
from collections import Counter


def create_dictionary(input_file):

    """This function creates a dictionary from input file in
     gene_names_from_chr21.py"""

    gene_dict = {}
    with open(input_file, 'r', encoding="utf-8") as infile:
        for line in infile:
            columns = line.strip().split()
            gene = columns[0]
            description = columns[1]
            gene_dict[gene] = description
    return gene_dict


def create_dictionary_1(input_file1):

    """This function creates a dictionary from first input file
     in find_common_cats.py"""

    gene_dict1 = {}
    with open(input_file1, 'r', encoding="utf-8") as infile:
        column1 = infile.readline().rstrip('\n')
        gene_symbol = column1[0]
        category = column1[2]
        gene_dict1[gene_symbol] = category
    return gene_dict1


def create_dictionary_2(input_file2):

    """This function creates a dictionary from second input file
     in find_common_cats.py"""

    gene_dict2 = {}
    with open(input_file2, 'r', encoding="utf-8") as infile:
        column2 = infile.readline().rstrip('\n')
        category = column2[0]
        description = column2[1]
        gene_dict2[category] = description
    return gene_dict2


def category_count(gene_dict1):

    """This function counts the number of genes present
     in the input file"""

    gene_counter = Counter()
    for value_list in gene_dict1.items():
        gene_counter.update(value_list)
        return gene_counter


def create_list1(gene_list1):

    """This function creates a list of genes present in
     the first input file"""

    with open(gene_list1, "r", encoding="utf-8") as gene_list:
        column_data1 = []
        for line in gene_list:
            columns1 = line.split()
            column_data1.append(columns1[0])
        return column_data1


def create_list2(gene_list2):

    """This function creates a list of genes present in
     the second input file"""

    with open(gene_list2, "r", encoding="utf-8") as gene_list:
        column_data2 = []
        for line in gene_list:
            columns2 = line.split()
            column_data2.append(columns2[0])
        return column_data2


def name_intersection(column_data1, column_data2):

    """This function finds the intersection between two lists"""

    shared_names = column_data1.intersection(column_data2)

    return shared_names


def name_difference_data1(column_data1, column_data2):

    """This function finds the difference between two lists"""

    unique_data = len(column_data1.difference(column_data2))

    return unique_data


def name_difference_data2(column_data2, column_data1):

    """This function finds the difference between two lists"""

    unique_data = len(column_data1.difference(column_data2))

    return unique_data
