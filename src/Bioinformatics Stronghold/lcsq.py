#   Finding a Shared Spliced Motif
'''
Given: Two DNA strings s and t (each having length at most 1 kbp) in FASTA format.

Return: A longest common subsequence of s and t. (If more than one solution exists,
you may return any one.)
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

def alignment_matrix(a:str, b:str)->list:
    a_len, b_len = len(a)+1 , len(b)+1 #rows AACCTTGG, #cols ACACTGTGA
    
    M = [[0] * b_len  for i in range(a_len)]

    for i in range(1, a_len): #rows
        for j in range(1, b_len): #cols
            up = M[i-1][j]
            left = M[i][j-1]
            diagonal = M[i-1][j-1]

            if a[i-1] == b[j-1]:
                M[i][j] = max(up, left, diagonal+1)
            else:
                M[i][j] = max(up, left, diagonal)
    return M

def main():
    seqs = """>Rosalind_23
AACCTTGG
>Rosalind_64
ACACTGTGA""".splitlines()
    seqs_dict=fasta_to_dict(seqs)
    a, b = seqs_dict.values()

    mat = alignment_matrix(a, b)
    i,j = len(a), len(b) #i is vertical, j is horizontal 

    sequence = []
    while i != 0 and j != 0:
        if mat[i][j] == mat[i][j-1]:
            j-=1
        elif mat[i][j] == mat[i-1][j]:
            i-=1
        else:
            if a[i-1] == b[j-1]:
                sequence.append(a[i-1])
            i-=1
            j-=1

    print("".join(sequence), a, b)











if __name__ == "__main__":
    main()