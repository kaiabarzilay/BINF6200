Kaia Barzilay
~
BINF6200 - Assignment 3

## Program #1 -test_secondary_structure_splitter.py

### Overview

This program takes a fasta file of protein sequences and secondary structure, and returns two files.

### Description

This program test_secondary_structure_splitter.py takes as its input a fasta file containing both protein sequences and corresponding secondary structure data for a group of unknown proteins. The output of this program are two files, with one containing the protein sequences and headers and one containing the secondary structure and headers. Within this program there are a series of functions.

The get_fasta_lists() function takes this fasta file as input and places all header data into a list called list_headers and places all sequence data into a list called list_seqs. Within this function the _verify_lists() function verifys that the two lists are of equal size. If they are not, the program exits.

The output_results_to_files() function takes the two lists of sequence and header data and outputs two files. The pdb_protein.fasta file will contain all header and sequence data for the protein data, and the pdb_ss.fasta file will contain all header and sequence data for the secondary structure data.

### Executing program in command line

```
$ python3 secondary_structure_splitter.py --infile ss.txt
```
```
$ python3 secondary_structure_splitter.py --infile ss_designed2Fail.txt
```

## Program #2 - nt_fasta_stats.py

### Overview

This program takes a fasta file and outputs statistics including the number of A's, T's, G's, C's, and any N's, as well as the length of the sequence and also the %GC content of the entire sequence.

### Description

This program nt_fasta_stats.py takes as its input a fasta file containing both protein sequences and corresponding secondary structure data for a group of unknown proteins. The output of this program are descriptive statistics, including the number of A's, T's, G's, C's, and any N's, as well as the length of the sequence and also the %GC content of the entire sequence. Within this program there are a series of functions.

The get_fasta_lists() function takes this fasta file as input and places all header data into a list called list_headers and places all sequence data into a list called list_seqs. Within this function the _verify_lists() function verifies that the two lists are of equal size. If they are not, the program exits.

The print_sequence_stats() function calls within it the _get_ncbi_accession() function, which takes as its input these two lists and checks that the sequence list only contains 'A' or 'G' or 'C' or 'T' or 'N'. If this isn't the case, the program exits. The _get_ncbi_accession() function within this function goes through the header and list and retrieves the accession number of the sequence. The print_sequence_stats() program prints the top line of the output, and each sequence's numerical values to the output file.

### Executing program in command line

```
$ python3 nt_fasta_stats.py
```
```
$ python3 nt_fasta_stats.py --infile influenza.fasta
```