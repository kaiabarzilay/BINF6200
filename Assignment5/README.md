BINF6200 Assignment 5 ~ Kaia Barzilay

# Assignment Description
For this assignment a program called main.py was created to combine  information from Human CCDS FASTA data set, with CCDS attributes  and ensembl gene data . Based on these files additional attributes are calculated, and output is printed to an Excel file. This assignment involves the implementation of various modules and functions for running.
## Main Python Program: main.py

### Overview
This is the main program for this assignment, which calls all other modules and functions. It calculates the output and prints to Excel file.
### Description
In this program four files are taken as input: a fasta file (CCDS_nucleo!de.current.fna), an attribute file (CCDS.current.txt), an ensemble gene file (ensembl_gene_data.tsv) and an output excel file (sequence_attributes.xlsx). Information from all three files is combined into a dataframe, which is then sorted based on amino acid Proline content. This is done in order to see what proteins in the human CCDS FASTA set have the highest and lowest Proline content. The top 10 highest and 10 lowest content proteins are printed to an output Excel file. In order to calculate all attributes such as Proline content modules fasta_format.py and seq_attributes_utils.py are imported.
### Example implementation at the command line
```
$ python3 -m sequence_attributes.main --infile_ccds_fasta sequence_attributes/inputs/CCDS_nucleotide.current.fna \
--infile_ccds_attributes sequence_attributes/inputs/CCDS.current.txt \
--infile_ensembl_gene sequence_attributes/inputs/ensembl_gene_data.tsv \
--excel_outfile sequence_attributes.xlsx
```
## Implemented module: fasta_format.py

### Overview
This module is contained within the sequence attributes module and is imported into the main.py file. It contains two functions: get_fasta_lists() and verify_lists(). The get_fasta_lists() is imported into main.py.
### Description
1. get_fasta_lists() -- this function takes as input a fasta file, which is read line by line. Two lists are created, with one containing all the headers from the fasta file, and one containing all the sequence data from the fasta file. The two lists match up one to one. This function returns the two lists as a tuple.
2. verify_lists() -- this function is called within the get_fasta_lists() function and checks that the two lists are the same length. If they are the function passes. If not, the program exits.
### Example implementation within main.py
```
from sequence_attributes import get_fasta_lists
```
## Implemented module: seq_attribute_utils.py

### Overview
This module is contained within the sequence attributes module and is imported into the main.py file. It contains 9 functions: gc_content(), lookup_by_ccds(), get_tm_from_dna_sequence(), get_sequence_composition(), calculate_amino_acid_content(), extract_kmers(), return_standard_genetic_code(), protein_translation() and get_additional_sequence_attributes(). The get_additional_sequence_attributes() and  return_standard_genetic_code() function are imported into main.py, all others are used within the get_additional_sequence_attributes() function.
### Description
1. gc_content() -- this function takes as input a dna sequence, a round_to value and a percentage. It calculated the percentage of the sequence that contains G or C bases. This function returns a float of this gc content.
2. lookup_by_ccds() -- this function takes as input a ccds id, a chrom and a dataframe (input from the return_standard_genetic_code() function). The input data frame is checked for matches to the ccds id and chrom, and these matches are then merged into a new dataframe. This function returns the data frame.
3. get_tm_from_dna_sequence() -- this function takes as input a sequence and a round_to value. The tm for the sequence is calculated using the output from the gc_content() function. It returns the tm value as a float.
4. get_sequence_composition() -- this function takes as input either a string, list or tuple sequence. It returns a dictionary of base occurances for the string.
5. calculate_amino_acid_content() -- this function takes as input an amino acid, a sequence and a round_to value. It calculates how many times the given amino acid appears in the sequence, and returns the percent of this amino acid in the sequence.
6. extract_kmers() -- this function takes as input a sequence and kmer size. It extracts the kmers from the sequence that are the indicated size and returns a list.
7. return_standard_genetic_code() -- this function returns the genetic code to be used in other functions, as indicated.
8. protein_translation() -- this function takes as input a string and translates it into a string of amino acids using the dictionary from the previous return_standard_dictionary() function. It returns this protein sequence as a string.
9. get_additional_sequence_attributes() -- this function takes as input a header,dna sequence, genetic code and attribute data frame. It utilizes all other functions within this module in order to return attributes/values. These include: ccds_id, chrom, header, dna_sequence, len(dna_sequence), protein_sequence, protein_sequence_len nucleotide_comp, amino_acid_comp, kmers_comp,proline_comp, tm_val, gc_val, *ccds_attributes.
### Example implementation within main.py
```
from sequence_attributes import get_additional_sequence_attributes, return_standard_genetic_code
```
## Implemented module: io_utils.py

### Overview
This module is contained within the sequence attributes module and is imported into the fasta_format.py file. It contains the FileHandle class.
### Description
This module contains the FileHandler class, which is utilized within the fasta_format.py module in the get_fasta_lists() function in order to open the fasta input file. This allows the function to be able to interact with a file in the system, opening it and reading it.
### Example implementation within fasta_format.py
```
from sequence_attributes.utils.io_utils import FileHandler

```
