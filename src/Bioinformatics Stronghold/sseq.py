#   Finding a Spliced Motif   
'''
Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.

Return: One collection of indices of s in which the symbols of t appear as a 
subsequence of s. If multiple solutions exist, you may return any one.
'''
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

def motif_spliced(s:str, t:str)->list:
    s_len, t_len = len(s), len(t)
    idxs = []
    j = 0
    for i in range(t_len):
        while s_len>j:
            if t[i]==s[j]:
                idxs.append(j+1)
                j += 1
                break
            j += 1
    return idxs

def main():
    dna = '''
>Rosalind_14
ACGTACGTGACG
>Rosalind_18
GTA
'''.splitlines()
    dna_dict = fasta_to_dict(dna)
    dna_list = list(dna_dict.values())
    m = motif_spliced(dna_list[0], dna_list[1])
    print(*m)

if __name__ == "__main__":
    main()
