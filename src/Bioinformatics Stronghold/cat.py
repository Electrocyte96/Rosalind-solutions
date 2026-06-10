#   Catalan Numbers and RNA Secondary Structures
'''
Given: An RNA string s having the same number of occurrences of 'A' as 'U' and the
same number of occurrences of 'C' as 'G'. The length of the string is at most 300 bp.

Return: The total number of noncrossing perfect matchings of basepair edges in the 
bonding graph of s, modulo 1,000,000.
'''
def is_complement(base1: str, base2: str)->bool:
    pair = base1 + base2 
    return pair in ("AU", "UA", "CG", "GC")

def main():
    rna = 'AUAUAU'
    print(rna)
    for i in range(len(rna)):
        for j in range(len(rna)):
            if i!=j:
                if is_complement(rna[i],rna[j]):
                    print('when ', rna[i],i, 'and',rna[j],j, 'interna:', rna[1:j], 'externa: ', rna[j+1:], is_complement(rna[i],rna[j]))


if __name__ == "__main__":
    main()