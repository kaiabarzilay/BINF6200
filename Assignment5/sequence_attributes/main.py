"""
This program takes in four argument () and
reads the data into pandas dataframes, merges them, and then
stores the data as tuples in a list. This list of tuples is then
turned into a dataframe once again and written to an Excel sheet.
The top 10 genes with the highest and lowest Proline count are
printed to an output file.
"""

import argparse
import sys
import pandas as pd
from sequence_attributes import get_fasta_lists, \
    get_additional_sequence_attributes, return_standard_genetic_code


def main():  # pragma: no cover

    """Business Logic"""

    args = get_cli_args()
    fasta_file = args.fasta_file
    ccds_attributes_file = args.infile_ccds_attributes
    ensembl_gene_file = args.infile_ensembl_gene
    outfile = args.excel_outfile

    # Read the attributes/ensemble file into pandas data frames.
    # Rename columns
    ccds_df = pd.read_csv(ccds_attributes_file, sep='\t')
    ccds_df.rename(columns={'gene_id': 'refseq_gene_id', '#chromosome': 'chrom'}, inplace=True)
    ensemble_df = pd.read_csv(ensembl_gene_file, sep='\t')
    ensemble_df.rename(columns={'ID': 'ensembl_gene_id',
                                'Canonical Transcript': 'ensembl_canonical_transcript_id',
                       'Gene': 'gene', 'Description': 'description', 'Biotype': 'biotype'},
                       inplace=True)

    # Merge dataframes
    merged_df = pd.merge(ccds_df, ensemble_df, how='left', on='gene')

    # Get the fasta data from the FASTA file data
    seq_header, sequence = get_fasta_lists(fasta_file)
    # Store tuple of headers and seq in a list
    all_data = []
    for i, (header, dna_sequence) in enumerate(zip(seq_header, sequence)):
        all_data.append(get_additional_sequence_attributes(header=header, dna_sequence=dna_sequence,
                                                           genetic_code=return_standard_genetic_code(),
                                                           attribute_df=merged_df))

        assert all_data[-1] is not None, "Failed to process sequence"
        if i == sys.maxsize:
            break
    # Convert list into dataframe, sort values.
    tuple_df = pd.DataFrame(all_data)
    tuple_df.sort_values(by=['proline_comp', 'protein_sequence_len'], ascending=[False, True],
                         inplace=True)
    # Print data frame to excel file
    tuple_df.to_excel(outfile, index=False)
    # Find 10 genes with highest/lowest proline composition
    proline_top_10 = tuple_df.sort_values(by='proline_comp', ascending=False).head(10)
    proline_bottom_10 = tuple_df.sort_values(by='proline_comp', ascending=True).tail(10)
    # Choose columns to print
    columns_to_select = ['ccds', 'refseq_gene_id', 'biotype', 'ensembl_gene_id',
                         'description', 'protein_sequence_len', 'proline_comp']
    # Get columns from data frames
    proline_top_10 = proline_top_10[columns_to_select]
    proline_bottom_10 = proline_bottom_10[columns_to_select]
    combined_proline_df = pd.concat([proline_top_10, proline_bottom_10])
    # Print merged data frames to output file
    if outfile.endswith('.xlsx'):
        outfile = outfile.replace('.xlsx', '.tsv')
    elif not outfile.endswith('.tsv'):
        outfile = outfile + '.tsv'
    combined_proline_df.to_csv(outfile, sep='\t', index=False)


def get_cli_args() -> argparse.Namespace:  # pragma: no cover

    """
    Just get the command line options using argparse
    @return: Instance of argparse arguments
    """

    parser = (argparse.ArgumentParser
              (description='Provide a FASTA file to generate coding statistics'))

    parser.add_argument('--infile_ccds_fasta',
                        dest='fasta_file',
                        type=str,
                        help='CCDS fna file to open (FASTA format)',
                        required=True,
                        default='sequence_attributes/inputs/CCDS_nucleotide.current.fna')

    parser.add_argument('--infile_ccds_attributes',
                        dest='infile_ccds_attributes',
                        type=str,
                        help='CCDS attributes file to open',
                        required=True,
                        default='sequence_attributes/inputs/CCDS.current.txt')

    parser.add_argument('--infile_ensembl_gene',
                        dest='infile_ensembl_gene',
                        type=str,
                        help='Ensembl gene information file to open',
                        required=True,
                        default='sequence_attributes/inputs/ensembl_gene_data.tsv')

    parser.add_argument('--excel_outfile',
                        dest='excel_outfile',
                        type=str,
                        help='Excel file to write final output',
                        required=True,
                        default='sequence_attributes.xlsx')

    return parser.parse_args()


if __name__ == '__main__':  # pragma: no cover
    main()
