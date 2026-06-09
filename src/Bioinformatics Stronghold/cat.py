#   Catalan Numbers and RNA Secondary Structures
'''
Given: An RNA string s having the same number of occurrences of 'A' as 'U' and the
same number of occurrences of 'C' as 'G'. The length of the string is at most 300 bp.

Return: The total number of noncrossing perfect matchings of basepair edges in the 
bonding graph of s, modulo 1,000,000.
'''
def can_pair(base1: str, base2: str) -> bool:
    pair = base1 + base2 
    return pair in ("AU", "UA", "CG", "GC")

def main():
    dna = 'AUAU'
    for i in range(len(dna)):
        for j in range(len(dna)):
            if i!=j:
                print(dna[i],dna[j], can_pair(dna[i],dna[j]),)
        

if __name__ == "__main__":
    main()