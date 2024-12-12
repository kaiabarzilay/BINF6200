"""protein_to_daltons.py"""

def main():

    """This code takes an amino acid sequence as an input and outputs its weight in kilodaltons"""

    # amino acid sequence of Protein kinase C beta
    protein_sequence = ("MADPAAGPPPSEGEESTVRFARKGALRQKNVHEVKNHKFTARFFKQPTFCSHCTDFIWGFGKQGFQCQVCCFVV"
        "HKRCHEFVTFSCPGADKGPASDDPRSKHKFKIHTYSSPTFCDHCGSLLYGLIHQGMKCDTCMMNVHKRCVMNVPSLCGTDHTERRGRIYI"
        "QAHIDREVLIVVVRDAKNLVPMDPNGLSDPYVKLKLIPDPKSESKQKTKTIKCSLNPEWNETFRFQLKESDKDRRLSVEIWDWDLTSRND"
        "FMGSLSFGISELQKAGVDGWFKLLSQEEGEYFNVPVPPEGSEGNEELRQKFERAKIGQGTKAPEEKTANTISKFDNNGNRDRMKLTDFNF"
        "LMVLGKGSFGKVMLSERKGTDELYAVKILKKDVVIQDDDVECTMVEKRVLALPGKPPFLTQLHSCFQTMDRLYFVMEYVNGGDLMYHIQQ"
        "VGRFKEPHAVFYAAEIAIGLFFLQSKGIIYRDLKLDNVMLDSEGHIKIADFGMCKENIWDGVTTKTFCGTPDYIAPEIIAYQPYGKSVDW"
        "WAFGVLLYEMLAGQAPFEGEDEDELFQSIMEHNVAYPKSMSKEAVAICKGLMTKHPGKRLGCGPEGERDIKEHAFFRYIDWEKLERKEIQ"
        "PPYKPKARDKRDTSNFDKEFTRQPVELTPTDKLFIMNLDQNEFAGFSYTNPEFVINV")

    print(protein_sequence)

    # find the number of amino acids in the sequence
    number_of_amino_acids = len(protein_sequence)

    # calculate the molecular weight of the protein in kilodaltons
    average_molecular_weight = (number_of_amino_acids * 110) / 1000

    # print number of amino acids
    print('\nThe length of "Protein kinase C beta type" is:',number_of_amino_acids)

    # print weight of protein in kilodaltons
    print('The average weight of this protein sequence in kilodaltons is:',average_molecular_weight)

main()
