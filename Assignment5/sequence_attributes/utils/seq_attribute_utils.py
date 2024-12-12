"""Module with functions to be implemented in main.py"""

from collections import namedtuple, Counter
import math
from typing import Union
import pandas as pd


def gc_content(sequence: str, round_to: int = 2, percentage: bool = True) -> float:

    """
    This function calculated the GC content of a sequence.
    :param sequence: The sequence to be analyzed.
    :param round_to: Round the GC content to this many bases.
    :param percentage: Percentage.
    :return: GC content of the sequence.
    """

    # count the G and Cs in the sequence string
    gc_count = sequence.count('G') + sequence.count('C')
    # calculate the fraction of sequence that is G and Cs
    gc_fraction = gc_count / len(sequence)
    # test
    assert gc_content('ATTTTTAAAA', round_to=2, percentage=True) == 0.0, "sequence contains no G or C"
    # return content as percentage or fraction based on input
    if percentage:
        return round(gc_fraction * 100, round_to)
    return round(gc_fraction, round_to)


def lookup_by_ccds(ccds_id: str, chrom: str, df: pd.DataFrame) -> pd.DataFrame:

    """
    This function filters a given pandas dataframe and returns a pandas
    dataframe that contains matching ccds_id and chrom being looked for.
    :param ccds_id: The id of the ccds being looked for.
    :param chrom: The chromosome being looked for.
    :param df: The dataframe to be filtered.
    :return: The filtered dataframe.
    """

    # make sure ccds_id and chrom are uppercase
    ccds_id = ccds_id.upper()
    chrom = chrom.upper()
    # create new df that matches input ccds and chrom columns
    new_df = df[(df.chrom == chrom) & (df.ccds_id == ccds_id)]
    test_df = pd.DataFrame()
    # test
    assert not lookup_by_ccds('CCDS2.2', '1', test_df).empty, "df is empty and shouldn't be"
    return new_df


def get_tm_from_dna_sequence(sequence: str, round_to: int = 2) -> float:

    """
    Given a DNA sequence this function returns the meltng temperature
    (Tm) for a set of DNA sequences based on the nearest-neighbor model.
    :param sequence: The DNA sequence to be analyzed.
    :param round_to: Round to this many bases.
    :return: The meltng temperature.
    """

    # make sure DNA sequence is all uppercase, as well as sequence length
    sequence = sequence.upper()
    seq_length = len(sequence)
    # use the previous gc_content function to calculate gc content of input seq
    sequence_gc_content = gc_content(sequence, round_to=round_to)
    # equation to calculate tm of sequence, using Na concentration and log Na concentration
    na_concentration = 50
    log_na_concentration = math.log10(na_concentration)
    tm_value = 81.5 + 16.6 * log_na_concentration + 0.41 * sequence_gc_content - (600 / seq_length)
    # test
    dna = 'AGCT'
    assert get_tm_from_dna_sequence(dna) == 8.9, f"TM of {dna} is not 8.9"
    return round(tm_value, round_to)


def get_sequence_composition(sequence: Union[str, list, tuple]) -> dict:

    """
    This function takes a DNA sequence and returns a dictionary for each
    occurrence in the string, list, or tuple.
    :param sequence: The DNA sequence to be analyzed.
    :return: A dictionary for each occurrence in the string.
    """

    # make sure input sequence is upper
    sequence = sequence.upper()
    # create base dictionary
    seq_dict = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
    # loop over sequence and input into dictionary
    for base in sequence:
        if base in seq_dict:
            seq_dict[base] += 1
    # test
    assert get_sequence_composition('ATGCGA') == {'A': 2, 'T': 1, 'G': 2, 'C': 1}
    return seq_dict


def calculate_amino_acid_content(amino_acid: str, sequence: str,
                                 round_to: int = 2, percentage: bool = True) -> float:

    """
    This function takes a sequence and returns either the fraction of or
    percentage of the amino acid in the sequence passed into the function
    :param amino_acid: The amino acid to be analyzed.
    :param sequence: The DNA sequence to be analyzed.
    :param round_to: Round to this value.
    :param percentage: Percentage.
    :return: Percentage/Fraction of amino acid in the sequence.
    """

    # make sure input aa and seq are upper. Calculate seq length.
    amino_acid = amino_acid.upper()
    sequence = sequence.upper()
    seq_length = len(sequence)
    amino_acid_count = 0
    # loop over seq and if it matches input amino acid, add to count
    for letter in sequence:
        if letter == amino_acid:
            amino_acid_count += 1
        else:
            pass
    # calculate % of amino acid in input seq
    percentage = amino_acid_count / seq_length * 100
    # test
    assert calculate_amino_acid_content('P', 'APPP PPP PPP PPPAP P P P') == 66.67
    return round(percentage, round_to)


def extract_kmers(sequence: str, kmer_size: int = 3) -> list:

    """
    This function takes a DNA sequence and returns a list of kmers.
    :param sequence: The DNA sequence to be analyzed.
    :param kmer_size: The size of the kmers.
    :return: A list of kmers.
    """

    # create lisr of kmers from input sequence based on input size
    kmer_list = [sequence[i: i + kmer_size] for i in range(len(sequence) - kmer_size + 1)]
    # test
    assert extract_kmers('ATGCGA', 3) == ['ATG', 'TGC', 'GCG', 'CGA']
    return kmer_list


def return_standard_genetic_code() -> dict:

    """
    This function returns genetic code as dictionary.
    :return: A dictionary for genetic code.
    """

    return {
        "UUU": "F", "UUC": "F", "UCU": "S", "UCC": "S", "UAU": "Y", "UAC": "Y",
        "UGU": "C", "UGC": "C", "UUA": "L", "UCA": "S", "UAA": None, "UGA": None,
        "UUG": "L", "UCG": "S", "UAG": None, "UGG": "W", "CUU": "L", "CUC": "L",
        "CCU": "P", "CCC": "P", "CAU": "H", "CAC": "H", "CGU": "R", "CGC": "R",
        "CUA": "L", "CUG": "L", "CCA": "P", "CCG": "P", "CAA": "Q", "CAG": "Q",
        "CGA": "R", "CGG": "R", "AUU": "I", "AUC": "I", "ACU": "T", "ACC": "T",
        "AAU": "N", "AAC": "N", "AGU": "S", "AGC": "S", "AUA": "I", "ACA": "T",
        "AAA": "K", "AGA": "R", "AUG": "M", "ACG": "T", "AAG": "K", "AGG": "R",
        "GUU": "V", "GUC": "V", "GCU": "A", "GCC": "A", "GAU": "D", "GAC": "D",
        "GGU": "G", "GGC": "G", "GUA": "V", "GUG": "V", "GCA": "A", "GCG": "A",
        "GAA": "E", "GAG": "E", "GGA": "G", "GGG": "G"
    }


def protein_translation(sequence: str, genetic_code: dict) -> str:

    """
    This function returns a string of the nucleic acid sequence (sequence) converted
    into protein sequence, until the end or until it comes across a stop codon.
    :param sequence: The DNA sequence to be analyzed.
    :param genetic_code: The genetic code of the DNA sequence to be analyzed.
    :return: The protein sequence.
    """

    # input genetic code is from the return_standard_genetic_code function above.
    genetic_code = return_standard_genetic_code()
    rna_sequence = sequence.replace('T', 'U')
    translated_sequence = []
    # loop over input seq and use dict to translate each codon into aa counterpart.
    # append translated seq to list.
    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i: i + 3]
        if codon in genetic_code:
            amino_acid = genetic_code[codon]
            if amino_acid is None:
                break
            translated_sequence.append(amino_acid)
    # test
    assert protein_translation('ATGTCCAAGGGGATCCTGCAGGTGCATCCTCCGATCTGCGACTGCCCGGGCTGCCGAATA',
                               genetic_code) == 'MSKGILQVHPPICDCPGCRI'
    return ''.join(translated_sequence)


def get_additional_sequence_attributes(header: str = None, dna_sequence: str = None,
                                       genetic_code: dict = None, attribute_df: pd.DataFrame = None) -> namedtuple:
    """
    Get the additional attributes for the Header and DNA sequence passed in
    :param header: FASTA header
    :param dna_sequence: FASTA sequence
    :param genetic_code: dictionary where key = codon and key = amino acid
    :param attribute_df: The attribute data frame (gene level information)
    :return: namedtuple
    """

    ccds_id, _, chrom = header.split("|")
    chrom = chrom.replace('chr', '')

    ccds_entry_df = lookup_by_ccds(ccds_id=ccds_id, chrom=chrom, df=attribute_df)
    assert len(ccds_entry_df) == 1, f"Data frame for ccds {ccds_id} is not length of 1"

    # Define the attributes for the named tuple
    ccds_attributes_to_get = ['nc_accession', 'gene', 'refseq_gene_id', 'biotype',
                              'ensembl_gene_id',
                              'ensembl_canonical_transcript_id', 'description']
    tuple_fields = ['ccds', 'chrom', 'header', 'dna_sequence', 'dna_sequence_len',
                    'protein_sequence',
                    'protein_sequence_len', 'nucleotide_comp', 'amino_acid_comp',
                    'kmers_comp',
                    'proline_comp', 'tm', 'gc'] + ccds_attributes_to_get

    # Create the named tuple type
    FastaTuple = namedtuple("FastaTuple", tuple_fields)

    # 1. Extract 3-mers from the DNA sequence
    kmers = extract_kmers(sequence=dna_sequence, kmer_size=3)

    # 2. Translate the DNA sequence to a protein sequence
    protein_sequence = protein_translation(dna_sequence, genetic_code)
    protein_sequence_len = len(protein_sequence)

    # 3. Get the TM of the DNA sequence
    tm_val = get_tm_from_dna_sequence(dna_sequence, round_to=2)

    # 4. Compute compositions for nt, amino acids, and kmers
    nucleotide_comp = Counter(dna_sequence)
    amino_acid_comp = Counter(protein_sequence)
    kmers_comp = Counter(kmers)

    # 5 Get GC content
    gc_val = gc_content(dna_sequence)  # pylint: disable=invalid-name

    # 6 get CCDS attributes from the DF
    ccds_attributes = [ccds_entry_df[val].iloc[0] for val in ccds_attributes_to_get]

    # 7 find proline composition
    proline_comp = protein_sequence.count('P')

    # Instantiate and return the named tuple
    return FastaTuple(ccds_id, chrom, header, dna_sequence, len(dna_sequence), protein_sequence,
                      protein_sequence_len, nucleotide_comp, amino_acid_comp, kmers_comp,
                      proline_comp, tm_val, gc_val, *ccds_attributes)
