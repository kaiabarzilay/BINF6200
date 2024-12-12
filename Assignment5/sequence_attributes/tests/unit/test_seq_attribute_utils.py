"""Test script for seq_attribute_utils module."""

from collections import Counter
import pytest
import pandas as pd

from sequence_attributes import lookup_by_ccds, get_tm_from_dna_sequence, \
    get_additional_sequence_attributes, calculate_amino_acid_content, \
    extract_kmers, get_sequence_composition, return_standard_genetic_code, \
    protein_translation, gc_content


def test_no_gc_content():
    """Function to test gc_content() function."""

    # test function works for string of no G and C
    sequence1 = "ATTTTTAAAA"
    round_to = 2
    result = gc_content(sequence1, round_to, percentage=True)
    assert result == 0.00, ("Expected zero gc content, got", result)

    # test function works for string with only G and C
    sequence2 = "GGGGCCCCCC"
    result = gc_content(sequence2, round_to, percentage=True)
    assert result == 10.00, ("Expected 10 gc content, got", result)

    # test function works for normal string
    sequence3 = "GGGGTTAAACCCC"
    result = gc_content(sequence3, round_to, percentage=True)
    assert result == 8.00, ("Expected 8 gc content, got", result)

    # test function works for empty string
    sequence4 = ""
    result = gc_content(sequence4, round_to, percentage=True)
    assert result == 0.00, ("Expected zero gc content, got", result)


def test_lookup_by_ccds_match():
    """Function to test lookup_by_ccds() function when values match"""

    # create test df
    test_df = {
        'ccds_id': ['CCDS1.1', 'CCDS2.2', 'CCDS3.3'],
        'chrom': ['1', '1', '2'],
        'additional_column': ['value1', 'value2', 'value3']
    }
    test_df = pd.DataFrame(test_df)

    # test function for where values match df
    result1 = lookup_by_ccds('CCDS1.1', '1', test_df)
    assert not result1.empty, "The dataframe should not be empty"
    assert result1.shape[0] == 1, ("Expected 1 row but got", result1.shape[0])
    assert result1['ccds_id'].iloc[0] == 'CCDS2.2', "CCDS ID doesn't match"
    assert result1['chrom'].iloc[0] == '1', "Chromosome doesn't match"


def test_lookup_by_ccds_not_match():
    """Function to test lookup_by_ccds() function when values do not match"""

    # create test df
    test_df = {
        'ccds_id': ['CCDS1.1', 'CCDS2.2', 'CCDS3.3'],
        'chrom': ['1', '1', '2'],
        'additional_column': ['value1', 'value2', 'value3']
    }
    test_df = pd.DataFrame(test_df)

    # test function for where values do not match df
    result2 = lookup_by_ccds('CCDS5.5', '5', test_df)
    assert result2.empty, ("The dataframe should be empty when there is no match found"
                           "in the data frame")


def test_lookup_by_ccds_empty_df():
    """Function to test lookup_by_ccds() function when df is empty"""

    test_df = pd.DataFrame(columns=['ccds_id', 'chrom', 'other_column'])
    # test function for when df is empty
    result3 = lookup_by_ccds('CCDS1.1', '1', test_df)
    assert result3.empty, "The result dataframe should be empty for an empty original dataframe"


def test_lookup_by_ccds_case_insensitive():
    """Function to test lookup_by_ccds() function when case-sensitive"""

    # create test df
    test_df = {
        'ccds_id': ['CCDS1.1', 'CCDS2.2', 'CCDS3.3'],
        'chrom': ['1', '1', '2'],
        'additional_column': ['value1', 'value2', 'value3']
    }
    test_df = pd.DataFrame(test_df)

    # test function for where mixture of upper and lower letters
    result4 = lookup_by_ccds('ccds3.3', '2', test_df)
    assert not result4.empty, "The result dataframe should not be empty"
    assert result4['ccds_id'].iloc[0] == 'CCDS3.3', "CCDS ID doesn't match"
    assert result4['chrom'].iloc[0] == '2', "Chromosome doesn't match"


def test_lookup_by_ccds_empty_input():
    """Function to test lookup_by_ccds() function when ccds input is empty"""

    # create test df
    test_df = {
        'ccds_id': ['CCDS1.1', 'CCDS2.2', 'CCDS3.3'],
        'chrom': ['1', '1', '2'],
        'additional_column': ['value1', 'value2', 'value3']
    }
    test_df = pd.DataFrame(test_df)

    # test function for when there is empty input
    result5 = lookup_by_ccds('', '', test_df)
    assert result5.empty, "The result dataframe should be empty when empty string is passed"


def test_get_tm_from_dna_sequence():
    """Function to test get_tm_from_dna_sequence() function."""

    # test function for normal string w/o round_to
    result1 = get_tm_from_dna_sequence('AGCT')
    assert result1 == 8.9, ("Expected 8.9, got", result1)

    # test function for normal string with round_to
    result2 = get_tm_from_dna_sequence('AGCT', round_to=1)
    assert result2 == 8.9, ("Expected 8.9, got", result2)

    # test function for mixture of upper and lower letters
    result3 = get_tm_from_dna_sequence('AgcT')
    assert result3 == 8.9, ("Expected 8.9 when letters are mixed, got", result3)

    # raise error if dividing by 0
    with pytest.raises(ZeroDivisionError):
        get_tm_from_dna_sequence('')


def test_get_sequence_composition():
    """Function to test get_sequence_composition() function."""

    # test function for string
    result1 = get_sequence_composition('AGCT')
    assert result1 == {'A': 1, 'C': 1, 'T': 1, 'G': 1}, ("Expected", result1)
    # test function for list
    result2 = get_sequence_composition(['A', 'G', 'C', 'T'])
    assert result2 == {'A': 1, 'C': 1, 'T': 1, 'G': 1}, ("Expected", result2)
    # test function for set
    result3 = get_sequence_composition(('A', 'G', 'C', 'T'))
    assert result3 == {'A': 1, 'C': 1, 'T': 1, 'G': 1}, ("Expected", result3)
    # test function for empty string
    result4 = get_sequence_composition('')
    assert result4 == {'A': 0, 'T': 0, 'G': 0, 'C': 0}, ("Expected", result4)
    # test function for mixture of upper and lower letters
    result5 = get_sequence_composition('AgcT')
    assert result5 == {'A': 1, 'C': 1, 'T': 1, 'G': 1}, ("Expected", result5)


def test_calculate_amino_acid_content():
    """Function to test calculate_amino_acid_content() function."""

    # test function for normal input
    result1 = calculate_amino_acid_content('P', 'APPP PPP PPP PPPAP P P P', round_to=2)
    assert result1 == 66.67, ("Expected 66.67, got", result1)
    # test function for amino acid not appearing
    result2 = calculate_amino_acid_content('N', 'APPP PPP PPP PPPAP P P P', round_to=2)
    assert result2 == 0.0, ("Expected 0.0 amino acid content, got", result2)
    # test function for empty sequence string
    result3 = calculate_amino_acid_content('A', '', round_to=2)
    assert result3 == 0.0, ("Expected 0.0 amino acid content, got", result3)
    # test function for sequence string mixture of upper and lower letters
    result4 = calculate_amino_acid_content('P', 'aPp PpP PpPpp P Pp P', round_to=2)
    assert result4 == 66.67, ("Expected 66.67, got", result4)

    # raise error for string with special characters
    with pytest.raises(ValueError):
        calculate_amino_acid_content('P', 'APPP @PP P%P PPPAP P P P', round_to=2)


def test_extract_kmers():
    """Function to test extract_kmers() function."""

    # test function for normal string
    kmer_list1 = extract_kmers('ATGCGA', 3)
    assert kmer_list1 == ['ATG', 'TGC', 'GCG', 'CGA']
    # test function for string smaller than kmer size
    kmer_list2 = extract_kmers('ATGC', 10)
    assert kmer_list2 == [], ("Expected to get [] but got", kmer_list2)
    # test function for empty sequence
    kmer_list3 = extract_kmers('', 3)
    assert kmer_list3 == [], ("Expected [] but got", kmer_list3)
    # test function for special characters in string
    kmer_list4 = extract_kmers('ATGC$#GA', 3)
    assert kmer_list4 == ['ATG', 'TGC', 'GC$', 'C#$', '#$G', '$GA'], \
        ("Expected ['ATG', 'TGC', 'GC$', 'C#$', '#$G', '$GA'] but got", kmer_list4)


def test_return_standard_genetic_code():
    """Function to test return_standard_genetic_code() function."""

    # test function for returning expected dictionary
    aa_dict = {
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
    assert return_standard_genetic_code() == aa_dict, "Expected standard genetic code"


def test_protein_translation():
    """Function to test protein_translation() function."""

    # test function for normal string
    genetic_code = return_standard_genetic_code()
    sequence1 = 'ATGTCCAAGGGGATCCTGCAGGTGCATCCTCCGATCTGCGACTGCCCGGGCTGCCGAATA'
    protein_seq1 = 'MSKGILQVHPPICDCPGCRI'
    seq_translation1 = protein_translation(sequence1, genetic_code)
    assert seq_translation1 == protein_seq1, ("Expected 'MSKGILQVHPPICDCPGCRI' protein, got",
                                              seq_translation1)
    sequence2 = 'ATGTCCAAGGGGATCCTGCAGGTGCATCCTCCGATCTGCGACTGCCCGGGCTGCCGAATAG'
    protein_seq2 = 'MSKGILQVHPPICDCPGCRI'
    seq_translation2 = protein_translation(sequence2, genetic_code)
    assert seq_translation2 == protein_seq2, ("Expected 'MSKGILQVHPPICDCPGCRI' protein, got",
                                              seq_translation2)
    # test function for no valid combinations
    sequence3 = 'TGCATGAGTCAGTGG'
    expected_seq1 = ''
    seq_translation3 = protein_translation(sequence3, genetic_code)
    assert seq_translation3 == expected_seq1, ("Expected '', got", seq_translation3)

    # test function for non-valid letter
    sequence4 = 'CXG'
    expected_seq2 = ''
    seq_translation4 = protein_translation(sequence4, genetic_code)
    assert seq_translation4 == expected_seq2, ("Expected '', got", seq_translation4)

    # test function for stop codon
    sequence5 = 'ATGAGTGA'
    protein_seq3 = 'M'
    seq_translation5 = protein_translation(sequence5, genetic_code)
    assert seq_translation5 == protein_seq3, ("Expected 'M', got", seq_translation5)

    # test function for empty string
    sequence6 = ''
    protein_seq6 = ''
    seq_translation6 = protein_translation(sequence6, genetic_code)
    assert seq_translation6 == protein_seq6, ("Expected '', got", seq_translation6)


def test_get_additional_seq_attributes():
    """Function to test get_additional_seq_attributes() function."""

    # create test header, sequence, genetic code and df
    test_header = "CCDS3.3|some_other_info|3"
    test_dna_sequence = "ATGTCCAAGGGGAACCTGCAGGTGCCTCCTCCGATCTGGGACTGCCCGGTCTGCCGAATA"
    test_genetic_code = {'AUG': 'M', 'UCC': 'S', 'CGA': 'R'}
    test_df = {
        'gene': ['GENE3'],
        'chrom': ['3'],
        'refseq_gene_id': ['PR_002'],
        'biotype': ['protein_coding'],
        'ensembl_gene_id': ['ENSG000444'],
        'ensembl_canonical_transcript_id': ['ENST000666'],
        'description': ['Test gene description for CCDS3.3']
    }
    test_attribute_df = pd.DataFrame(test_df)

    # test function for proper output with test input
    test_result = get_additional_sequence_attributes(test_header,
                                                     test_dna_sequence, test_genetic_code,
                                                     test_attribute_df)
    # test function for returning a tuple
    assert isinstance(test_result, tuple)
    # test function for correct type
    assert hasattr(test_result, 'ccds'), ("Expected result to be a tuple, got", type(test_result))

    # make sure function returned the following correct output values:
    assert test_result.ccds == 'CCDS3.3', ("Expected ccds to be 'CCDS3.3', got", test_result.ccds)
    assert test_result.chrom == '3', ("Expected chrom to be 3, got", test_result.chrom)
    assert test_result.dna_sequence == test_dna_sequence, ("Expected dna sequence to be"
                                                           "'ATGTCCAAGGGGAACCTGCAGGTGCCTCCTCCGATCTGG"
                                                           "GACTGCCCGGTCTGCCGAATA'"
                                                           ", got", test_result.dna_sequence)
    assert test_result.protein_sequence == 'MSR', ("Expected protein sequence to be 'MSR', got",
                                                   test_result.protein_sequence)
    assert test_result.protein_sequence_len == 3, ("Expected protein sequence length to be 3, got",
                                                   test_result.protein_sequence_len)
    assert test_result.tm == 111.41, ("Expected tm to be 111.41, got", test_result.tm)
    assert test_result.gc == 29.82, ("Expected gc val to be 29.82, got", test_result.gc)
    assert test_result.proline_comp == 0, ("Expected proline comp to be 0, got",
                                           test_result.proline_comp)
    assert (test_result.nucleotide_comp ==
            {'A': 9, 'C': 12, 'G': 10, 'T': 8}), \
        ("Expected nucleotide comp to be '{'A': 9, 'C': 12, 'G': 10, 'T': 8}', got",
         test_result.nucleotide_comp)
    assert test_result.amino_acid_comp == {'M': 1, 'S': 1, 'R': 1}, \
        ("Expected amino acid comp to be '{'M': 1, 'S': 1, 'R': 1}',got",
         test_result.amino_acid_comp)
    assert isinstance(test_result.kmers_comp, Counter)
    assert 'ATG' in test_result.kmers_comp, "Expected 'ATG' to be in kmers composition"

    assert test_result.refseq_gene_id == 'PR_002', \
        "Expected refseq_gene_id to be 'PR_002'"
    assert test_result.biotype == 'protein_coding', \
        "Expected biotype to be 'protein_coding'"
    assert test_result.ensembl_gene_id == 'ENSG000444', \
        "Expected ensembl_gene_id to be 'ENSG000444'"
    assert test_result.ensembl_canonical_transcript_id == 'ENST000666', \
        "Expected ensembl_canonical_transcript_id to be 'ENST000666'"
    assert (test_result.description == 'Test gene description for CCDS3.3'
                                       "Expected description to be"
                                       " 'Test gene description for CCDS3.3'")


if __name__ == "__main__":
    pytest.main()
