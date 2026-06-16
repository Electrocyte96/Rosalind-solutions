#   Speeding Up Motif Finding
'''
Given: A DNA string s (of length at most 100 kbp) in FASTA format.

Return: The failure array of s.
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

def kmp(s:str)->list:
    i, j, n, ls_prefix = 1, 0, len(s), [0 for x in s]
    while i < n:
        if s[i] == s[j]:
            j += 1
            ls_prefix[i] = j
            i += 1
        else:
            if j == 0:
                i += 1
            else:
                j = ls_prefix[j-1]
    return ls_prefix

def main():
    dna_fas = '''>Rosalind_87
CAGCATGGTATCACAGCAGAG'''.splitlines()
    dna_dict = fasta_to_dict(dna_fas)
    s = ''.join(dna_dict.values())
    ls_kmp = kmp(s)
    print(*ls_kmp)
    
    #with open('output.txt', 'w') as file:
    #    file.write(" ".join(map(str, ls_kmp)))

if __name__ == "__main__":
    main()






