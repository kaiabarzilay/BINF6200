Kaia Barzilay 
~
BINF6200 Assignment #4: Working with Dictionaries and Lists/Sets

## Assignment description:

For this assignment three programs were created to analyze data found in the text files chr21_genes.txt, chr21_genes_categories.txt, and HUGO_genes.txt. Data from text files is organized into either dictionaries or lists/sets. These programs use functions found within the assignment4_utils.py module. They each contain three functions: main(), print_output() and get_cli_args(). They either print their results to the command line or to an output file.

## Program #1 - gene_names_from_chr21.py

### Overview:
This program asks a user to enter a gene symbol and then prints the genes description.
### Description:
This program takes data from the chr21_genes.txt text file. It contains columns of information about various genes. This program contains three functions: main(), print_output() and get_cli_args(). When this program is executed the user will input into the command line the name of the gene they would like information on, and then this program will use a function located in the assignment4_utils module to turn the file into a dictionary. The program will then find the matching gene name in the dictionary. If it exists, this program will print it's matching description to the command line. If the gene name doesn't exist in the dictionary, they it will notify the user. 
### Executing program in command line examples:
```
$ python3 gene_names_from_chr21.py -i chr21_genes.txt
```
```
$ python3 gene_names_from_chr21.py # runs by default
```
## Program #2 - find_common_cats.py

### Overview:
This program takes as input the text files chr21_genes.txt and chr21_genes_categories.txt, and it counts how many genes are in each category (1.1, 1.2, 2.1 etc.). The results are then printed in ascending order to an output file categories.txt.
### Description:
This program takes as input the text files chr21_genes.txt and chr21_genes_categories.txt. The chr21_genes.txt contains all the genes in each category, while the hr21_genes_categories.txt file contains the description for the genes. This program contains three functions: main(), print_output() and get_cli_args(). This program will use functions located in the assignment4_utils module to create two dictionary for each of the files, as well as count the number of occurrences of  each gene in each category (1.1, 1.2, 2.1 etc.) in the dictionaries. This program then prints to an output file named categories.txt with the categories  arranged in ascending order, as well as the occurrence for each category and the description of the gene.
### Executing program in command line examples:
```
$ python3 find_common_cats.py -i1 chr21_genes.txt -i2 chr21_genes_categories.txt
```
```
$ python3 find_common_cats.py # runs by default
```
## Program #3 - intersection_of_gene_names.py

### Overview:
This program finds all gene symbols that appear both in the chr21_genes.txt file and in the HUGO_genes.txt file. The symbols are then printed in alphabetical order to the intersection_output.txt text file. It also prints onto the terminal the common gene symbols.
### Description:
This program takes as input the two input files chr21_genes.txt file and  HUGO_genes.txt file. This program contains three functions: main(), print_output() and get_cli_args(). This program will use functions located in the assignment4_utils module to create two lists/sets for the gene symbols of the files. It will also use functions in this module to calculate the gene symbols that are shared between the lists, as well as the gene symbols that are unique to both lists individually. The symbols are then printed in alphabetical order to an output file called intersection_output.txt text file. The gene symbols shared between the lists are also printed to the terminal, as well as the gene symbols unique to each list.
### Executing program in command line examples:
```
$ python3 intersection_of_gene_names.py -i1 chr21_genes.txt -i2 HUGO_genes.txt
```
```
$ python3 intersection_of_gene_names.py -i1 hgnc_complete_set_reduced.txt -i2 HUGO_genes.txt
```

