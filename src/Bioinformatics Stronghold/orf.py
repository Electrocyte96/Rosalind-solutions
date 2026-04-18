#   Open Reading Frames
'''
Given: A DNA string s of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated 
from ORFs of s. Strings can be returned in any order.
'''
dna_seqs = '''
>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG
'''.splitlines()

def fasta_to_dict(dna_strings:str)->dict:
    seq_dict = {}
    seq=[]
    header = None
    for i in range(len(dna_strings)):
        if dna_strings[i].startswith('>'):
            if header:
                seq_dict[header] = ''.join(seq)
            header = dna_strings[i][1:]
            seq = []
        else:
            seq.append(dna_strings[i])
    if header:
        seq_dict[header] = ''.join(seq)
    return seq_dict

def to_rna(t:str)->str:
    return t.replace('T', 'U') 

def complement(s:str)->str:
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    s_complement = ''
    for nt in reversed(s):
        s_complement += complement[nt]
    return s_complement

def rna_to_prot(s:str)->str:
    codons = {'UUU': 'F',      'CUU': 'L',      'AUU': 'I',      'GUU': 'V',
    'UUC': 'F',      'CUC': 'L',      'AUC': 'I',      'GUC': 'V',
    'UUA': 'L',      'CUA': 'L',      'AUA': 'I',      'GUA': 'V',
    'UUG': 'L',      'CUG': 'L',      'AUG': 'M',      'GUG': 'V',
    'UCU': 'S',      'CCU': 'P',      'ACU': 'T',      'GCU': 'A',
    'UCC': 'S',      'CCC': 'P',      'ACC': 'T',      'GCC': 'A',
    'UCA': 'S',      'CCA': 'P',      'ACA': 'T',      'GCA': 'A',
    'UCG': 'S',      'CCG': 'P',      'ACG': 'T',      'GCG': 'A',
    'UAU': 'Y',      'CAU': 'H',      'AAU': 'N',      'GAU': 'D',
    'UAC': 'Y',      'CAC': 'H',      'AAC': 'N',      'GAC': 'D',
    'UAA': 'Stop',   'CAA': 'Q',      'AAA': 'K',      'GAA': 'E',
    'UAG': 'Stop',   'CAG': 'Q',      'AAG': 'K',      'GAG': 'E',
    'UGU': 'C',      'CGU': 'R',      'AGU': 'S',      'GGU': 'G',
    'UGC': 'C',      'CGC': 'R',      'AGC': 'S',      'GGC': 'G',
    'UGA': 'Stop',   'CGA': 'R',      'AGA': 'R',      'GGA': 'G',
    'UGG': 'W',      'CGG': 'R',      'AGG': 'R',      'GGG': 'G'} 
    n = len(s)
    k = 3
    protein = []
    for i in range(0, n, k):
        amino = s[i:i+3]
        if len(amino) == 3:
            if codons[amino] == 'Stop':
                break
            protein.append(codons[amino])
    return ''.join(protein)

def reading_frame(dna_dict:dict)->set:
    proteins = set()
    for key, value in dna_dict.items():
        dna_c = complement(value)
        rna_c = to_rna(dna_c)
        rna = to_rna(value)
        n,k = len(rna),3
        for i in range(n-k+1):
            cod = rna[i:i+k]
            if len(cod) == 3:
                if cod == 'AUG':
                    prot = rna_to_prot(rna[i:])
                    if len(prot)*3 <= n-i-k:
                        proteins.add(prot)
        for i in range(n-k+1):
            cod = rna_c[i:i+k]
            if len(cod) == 3:
                if cod == 'AUG':
                    prot = rna_to_prot(rna_c[i:])
                    if len(prot)*3 <= n-i-k:
                        proteins.add(prot)
        return proteins

def main():
    dna_dict = fasta_to_dict(dna_seqs)
    proteins = reading_frame(dna_dict)
    for prot in proteins:
        print(prot)

if __name__ == "__main__":
    main()