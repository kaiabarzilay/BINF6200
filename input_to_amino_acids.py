"""input_to_amino_acids.py"""

import sys
def main():

    """This code takes a DNA input and prints amino acid length and weight"""

    # user inputs name of DNA sequence
    sequence_name = input("\nPlease enter a name for the DNA sequence: ")

    # print input
    print('Your sequence name is:',sequence_name)

    # user inputs the length of DNA sequence
    sequence_length = input("Please enter the length of the sequence: ")

    # print input
    print('The length of the DNA sequence is:', float(sequence_length))

    # if the DNA sequence length is divisible by 3 with no remainder:
    if int(sequence_length) % 3 == 0:

        # divide the number of nucleotides by 3 to get the number of amino acids
        amino_acid_count = int(sequence_length) / 3

        # calculate the molecular weight of the protein in kilodaltons
        average_molecular_weight = (amino_acid_count * 110) / 1000

        # print length in amino acids
        print('The length of the decoded protein is:',amino_acid_count)

        # print weight in kilodaltons
        print('The average weight of the protein sequence is:',average_molecular_weight)

    # if the DNA sequence length is not divisible by 3:
    else:

        # print('Error: the DNA sequence is not a multiple of 3')
        print("\n\nError: the DNA sequence is not a multiple of 3", file = sys.stderr)

        sys.exit(1)

main()
