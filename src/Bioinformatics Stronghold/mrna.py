#   Inferring mRNA from Protein
'''
Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein
could have been translated, modulo 1,000,000. (Don't neglect the importance
of the stop codon in protein translation.)
'''
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

def get_count_codons(codons:dict)->int:
    codons_count = {}
    for amino in codons.values():
            codons_count[amino] = codons_count.get(amino, 0) + 1
    codon_stop = codons_count['Stop']
    return codons_count, codon_stop

def num_mrna(s:str)->int:
    codon_count,  stop_codons = get_count_codons(codons)
    for amino in s:
        stop_codons = (stop_codons * codon_count[amino] % 1000000)
    return stop_codons

def main():
    s = 'MA'
    print(num_mrna(s))

if __name__ == "__main__":
    main()