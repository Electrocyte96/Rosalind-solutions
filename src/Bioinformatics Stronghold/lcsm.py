#   Finding a Shared Motif
'''
Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you 
may return any single solution.)
'''
dna_strings = '''
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA
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

def shared_motif(s:str)->str:
    for seq in s.values():
            s_len = len(seq) 
            for k in range(s_len, 1, -1): 
                for i in range(s_len-k+1): 
                    if all(seq[i:i+k] in seq2 for seq2 in s.values()):
                        return seq[i:i+k]

def main():
    dna_seqs = fasta_to_dict(dna_strings)
    print(shared_motif(dna_seqs))

if __name__ == "__main__":
    main()