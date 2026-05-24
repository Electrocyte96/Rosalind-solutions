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
    k = min(len(s), len(t))
    k_2 = k//2
    for i in range(k, k_2, -1):
        if s[-i:] == t[:i]:
            return i
    return 0

def right_read(seq:str, seqs:list)->list:
    n = len(seqs)
    for i in range(n):
        if seq != seqs[i]:
            ovr = overlap(seq, seqs[i])
            if ovr:
                return seqs[i], i, ovr

def left_read(seq:str, seqs:list)->list:
    n = len(seqs)
    for i in range(n):
        if seq != seqs[i]:
            ovr = overlap(seqs[i], seq)
            if ovr:
                return seqs[i], i, ovr

def assemble(seqs:list)->str:
    seq = seqs.pop(0)
    while seqs:
        r = right_read(seq, seqs)
        if not r:
            break
        seq_over, i, i_ovr = r
        seq = seq + seq_over[i_ovr:]
        seqs.pop(i)
        
    while seqs:
        r  = left_read(seq, seqs)
        if not r:
            break
        seq_over, i, i_ovr = r
        seq = seq_over[:-i_ovr] + seq
        seqs.pop(i)
        
    return seq

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
    seqs = list(dna_dict.values())
    print(assemble(seqs))
    

if __name__ == "__main__":
    main()