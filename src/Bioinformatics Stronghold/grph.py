#   Overlap Graphs
'''
Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: The adjacency list corresponding to O3. You may return edges in any order.
'''
dna_seqs = '''
>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG
'''.splitlines()
k = 3

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

def suffix_prefix(dna_dict:dict, k:int)->list:
    edges = []
    for id, seq in dna_dict.items():
        for id2, seq2 in dna_dict.items():
            if seq != seq2:
                if seq[-k:] == seq2[:k]:
                    edges.append([id, id2])
    return edges

def main():
    dna_dict = fasta_to_dict(dna_seqs)
    edges = suffix_prefix(dna_dict, k)
    for edge in edges:
        print(*edge, sep=' ')

if __name__ == "__main__":
    main()