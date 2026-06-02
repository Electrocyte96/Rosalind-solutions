#   Transitions and Transversions
'''
Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).

Return: The transition/transversion ratio R(s1,s2).
'''
def fasta_to_dict(dna_seqs:str)->dict:
    seq_dict = {}
    seq=[]
    header = None
    for i in range(len(dna_seqs)):
        if dna_seqs[i].startswith('>'):
            if header:
                seq_dict[header] = ''.join(seq)
            header = dna_seqs[i][1:]
            seq = []
        else:
            seq.append(dna_seqs[i])
    if header:
        seq_dict[header] = ''.join(seq)
    return seq_dict

def traversion_transition_ratio(s:str, t:str):
    transition, traversion = 0,0
    if len(s) == len(t):
        for nt in range(len(s)):
            if s[nt] == 'A' and t[nt] == 'G' or s[nt] == 'G' and t[nt] == 'A':
                transition += 1
            elif s[nt] == 'C' and t[nt] == 'T' or s[nt] == 'T' and t[nt] == 'C':
                transition += 1
            elif s[nt] == 'A' and t[nt] == 'C' or s[nt] == 'A' and t[nt] == 'T':
                traversion += 1
            elif s[nt] == 'C' and t[nt] == 'A' or s[nt] == 'C' and t[nt] == 'G':
                traversion += 1
            elif s[nt] == 'T' and t[nt] == 'A' or s[nt] == 'T' and t[nt] == 'G':
                traversion += 1
            elif s[nt] == 'G' and t[nt] == 'C' or s[nt] == 'G' and t[nt] == 'T':
                traversion += 1
    return transition/traversion

def main():
    dna = '''
>Rosalind_0209
GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
AGTACGGGCATCAACCCAGTT
>Rosalind_2200
TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
GGTACGAGTGTTCCTTTGGGT
'''.splitlines()
    dna_dict = fasta_to_dict(dna)
    seqs = list(dna_dict.values())
    ratio = traversion_transition_ratio(seqs[0], seqs[1])
    print(f'{ratio:.11f}')

if __name__ == "__main__":
    main()