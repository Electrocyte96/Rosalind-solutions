#   Catalan Numbers and RNA Secondary Structures
'''
Given: An RNA string s having the same number of occurrences of 'A' as 'U' and the
same number of occurrences of 'C' as 'G'. The length of the string is at most 300 bp.

Return: The total number of noncrossing perfect matchings of basepair edges in the 
bonding graph of s, modulo 1,000,000.
'''
memo = {}

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

def is_complement(base1: str, base2: str)->bool:
    return base1 + base2  in ("AU", "UA", "CG", "GC")

def count_structures(rna:str)->int:
    if rna in memo:
        return memo[rna]
    if rna == '':
        return 1
    if len(rna) % 2 != 0:
        return 0
    if rna.count('A') != rna.count('U') or rna.count('C') != rna.count('G'):
        return 0
    total,n = 0,len(rna)
    first_base = rna[0]
    for i in range(1, n, 2):
        if is_complement(first_base, rna[i]):
            inner, outer = rna[1:i], rna[i+1:]
            inner_seqs, outer_seqs = (count_structures(inner)), (count_structures(outer))
            total += inner_seqs * outer_seqs
    memo[rna] = total
    return total

def main():
    rna_fas = '''>Rosalind_57
AUAU'''.splitlines()
    rna_dict = fasta_to_dict(rna_fas)
    rna = ''.join(rna_dict.values())
    print(count_structures(rna)%1000000)

if __name__ == "__main__":
    main()