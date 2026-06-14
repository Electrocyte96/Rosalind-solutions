#   k-Mer Composition
'''
Given: A DNA string s in FASTA format (having length at most 100 kbp).

Return: The 4-mer composition of s.
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

def enum_kmers(k:int)->list:
    keys = ['A', 'C', 'G', 'T']
    if k == 1:
        return keys
    final_perms = []
    for key in keys:
        subkeys = enum_kmers(k-1)
        for subkey in subkeys:
            final_perms.append(key + subkey)
    return final_perms

def freq_4mers(dna:list)->list:
    k, dna_len = 4, len(dna)
    kmers = enum_kmers(k)
    kmers_dict = {x:0 for x in kmers}
    for i in range(dna_len-k+1):
        if dna[i:i+k] in kmers_dict:
            kmers_dict[dna[i:i+k]]+=1
    return list(kmers_dict.values())

def main():
    dna_fas = '''>Rosalind_6431
CTTCGAAAGTTTGGGCCGAGTCTTACAGTCGGTCTTGAAGCAAAGTAACGAACTCCACGG
CCCTGACTACCGAACCAGTTGTGAGTACTCAACTGGGTGAGAGTGCAGTCCCTATTGAGT
TTCCGAGACTCACCGGGATTTTCGATCCAGCCTCAGTCCAGTCTTGTGGCCAACTCACCA
AATGACGTTGGAATATCCCTGTCTAGCTCACGCAGTACTTAGTAAGAGGTCGCTGCAGCG
GGGCAAGGAGATCGGAAAATGTGCTCTATATGCGACTAAAGCTCCTAACTTACACGTAGA
CTTGCCCGTGTTAAAAACTCGGCTCACATGCTGTCTGCGGCTGGCTGTATACAGTATCTA
CCTAATACCCTTCAGTTCGCCGCACAAAAGCTGGGAGTTACCGCGGAAATCACAG
'''.splitlines()
    dna_dict = fasta_to_dict(dna_fas)
    dna = ''.join(dna_dict.values())
    print(*freq_4mers(dna))

if __name__ == "__main__":
    main()