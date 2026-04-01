#   Consensus and Profile
'''
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)
'''
dna_strings = '''
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT
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

def profile(dict_dna:dict)->dict:
    seq_len = max(len(seq) for seq in dict_dna.values())
    profile = {'A':[0]*seq_len,'C':[0]*seq_len,'G':[0]*seq_len,'T':[0]*seq_len}
    seqs = dict_dna.values()
    for i in range(seq_len):
        for seq in seqs:
            nt = seq[i]
            profile[nt][i]+=1
    return profile

def consensus(profile_dna: dict) -> str:
    seq_len = len(profile_dna['A'])
    consensus = []
    for i in range(seq_len):
        nt = max(['A','C','G','T'], key=lambda x: profile_dna[x][i])
        consensus.append(nt)
    return ''.join(consensus)

def main():
    dict_dna = fasta_to_dict(dna_strings)
    profile_dna = profile(dict_dna)
    print(consensus(profile_dna))
    for nt, seqs in profile_dna.items():
        print(nt + ":", *seqs)

if __name__ == "__main__":
    main()