#   RNA Splicing
'''
Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns.
All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of s. 
(Note: Only one solution will exist for the dataset provided.)
'''
fas = '''
>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT
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

def to_rna(t:str)->str:
    return t.replace('T', 'U') 

def splice(s:str, sub_s:list)->str:
    n = len(s)
    for i in sub_s:
        k, j = len(i), 0
        final_s = []
        while j < n :
            if i == s[j:j+k]:
                j += k
            else:
                final_s.append(s[j])
                j += 1
        s = ''.join(final_s)
        n = len(s)
    return ''.join(final_s)

def main():
    dna_dic = fasta_to_dict(fas)
    all_seqs = list(dna_dic.values())
    s, sub_s = all_seqs[0], all_seqs[1:]
    final_s = splice(s, sub_s)
    rna_final = to_rna(final_s)
    print(rna_to_prot(rna_final))

if __name__ == "__main__":
    main()
