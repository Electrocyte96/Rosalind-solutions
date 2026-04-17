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

def reading_frame(dna_seqs:str)->set:
    dna_dict = fasta_to_dict(dna_seqs)
    total_prots = set()
    for key, value in dna_dict.items():
        rna = to_rna(value)
        dna_c = complement(value)
        rna_c = to_rna(dna_c)
        k, n = 3, len(rna)
        for i in range(n-k+1):
            met = rna[i:i+k]
            prot = []
            if met == 'AUG':
                for j in range(i,n,k):
                    cod = rna[j:j+k]
                    if len(cod) == 3: 
                        if codons[cod] == 'Stop':
                            break
                        else:
                            prot.append(codons[cod])
                prot = ''.join(prot)
                total_prots.add(prot)
        
        for i in range(n-k+1):
            met = rna_c[i:i+k]
            prot = []
            if met == 'AUG':
                for j in range(i,n,k):
                    cod = rna_c[j:j+k]
                    if len(cod) == 3: 
                        if codons[cod] == 'Stop':
                            break
                        else:
                            prot.append(codons[cod])
                prot = ''.join(prot)
                total_prots.add(prot)
                
    return total_prots

def main():
    print(reading_frame(dna_seqs))


if __name__ == "__main__":
    main()