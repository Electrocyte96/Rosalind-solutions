#   Genome Assembly as Shortest Superstring
'''
Given: At most 50 DNA strings of approximately equal length, not exceeding 1 kbp, in FASTA format (which represent reads deriving from the same strand of a single linear chromosome).

The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their length.

Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).
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

def overlap(s:str, t:str)->str:
    k = len(s)
    k_2 = int(k/2)
    for i in range(k, k_2, -1):
        if s[-i:] == t[:i]:
            return s + t[i:]

def main():
    dna_seqs = '''
>Rosalind_56
ATTAGACCTG
>Rosalind_57
CCTGCCGGAA
>Rosalind_58
AGACCTGCCG
>Rosalind_59
GCCGGAATAC
'''.splitlines()
    dna_dict = fasta_to_dict(dna_seqs)
    seqs =list(dna_dict.values())
    print(seqs)
    #print(seqs[0], seqs[2])
    for i in seqs:
        print('-----------')
        print(i)
        for j in seqs:
            if i != j:
                print(overlap(i,j))
    


if __name__ == "__main__":
    main()