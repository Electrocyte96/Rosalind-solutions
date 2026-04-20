#   Locating Restriction Sites
'''
Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the
string having length between 4 and 12. You may return these pairs in any order.
'''
dna_seqs = '''
>Rosalind_5644
GCGCCATCCGCGAGCAGCAGTAGCCAGAGGTATGAAACCGGGGGTTCCCGCGTTAGACCT
AGCGATACTCATCTGCTGTAATAAGGCACAGTAACCCATCTTATATGATCCTTTTCACTA
AGAACTCTCGTTGACTAAAGCGTGTTTAATGACTTCGTGCCGCTTGTGCAAGAAAAGGCT
CATCGCATCTTCCAAGACACATCGGAACTACTCGCGGCAGTTTGACTTAGGGCTCACGAT
AACAGTAATTTAGTCTGTACTGACACTATTAATGATAATCTCAAGAAGTCACAAGCTGGG
TCGCCATGTAATTGACACTCTTACAATAAAGGAGCCACACTGCTACCTGCGGAATGCTTC
GCGAAACAGTCGGATTTTAATTGAAACCTGTCGGTAGCAGGATGTGCATTCGGTTCGGTT
TTCGGTCTCAGAAGACATAATAATGCTGCATTAGCTCGAGGACGCGTCTAATTAACATGT
TAACAGTGGATGGAGAGCGTTCTAACAGGTCTCTATATCCATTCCGCATGATATGCCTAG
TAAGACCTAGAATCCAACACGGCATCCCGCCTCTCGGCCGTTGGAATCCCCTTATCCCCG
ACAAGCTGTACCAAAAAAGAATGCTACATCCCACAATCTCTCCGCCTCTAGACCTGAATT
GGAGTGTACCTGTCGCGCTTCGGATAATAATATATATAGCAGACGTGCTTTCATTTGGCG
TCCTATCCAAGGTCCCCTTAAGTTTAAACCTTGGTGCAGAGTAGTGTACCGTTTGACTCC
CATATTCAACCGCTCTTTCCGCCGGACGTTTTCGGTTTATACGGGTTGAGTCATATATCA
ATCCGATCGTAGTCGTGGGAGAGTGCAATACCGGCGCGAAAGCCCCCGTCTACGTGACCG
TTCGGCCACCAACTGGCCTTTTACATATTGTCGTAATTGGGCGGGATGGGGCGC
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

def complement(s:str)->str:
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    s_complement = ''
    for nt in reversed(s):
        s_complement += complement[nt]
    return s_complement

def rev_palindrome(dna_dict:dict)->list:
    for key, value in dna_dict.items():
        n = len(value)
        index_len = []
        for k in range(4,12+1):
            for i in range(n-k+1):
                substring = value[i:i+k]
                substring_c = complement(substring)
                if substring == substring_c:
                    index_len.append([i+1, k])
    return index_len

def main():
    dna_dic = fasta_to_dict(dna_seqs)
    i_len = rev_palindrome(dna_dic)
    for i in i_len:
        print(*i, sep=' ')

if __name__ == "__main__":
    main()