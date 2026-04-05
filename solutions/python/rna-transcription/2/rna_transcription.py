"""
    Your task is to determine the RNA complement of a given DNA sequence.
"""

def to_rna(dna_strand):
    """
        Both DNA and RNA strands are a sequence of nucleotides.
        G -> C
        C -> G
        T -> A
        A -> U
    """

    result = ""
    dna_nucleotide = ["G", "C", "T", "A"]
    rna_nucleotide = ["C", "G", "A", "U"]
    for strand in dna_strand:
        result += rna_nucleotide[dna_nucleotide.index(strand)]
    return result
