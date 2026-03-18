#   Complementing a Strand of DNA
'''
Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
'''
def complement(s:str)->str:
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    s_complement = ''
    for nt in reversed(s):
        s_complement += complement[nt]
    return s_complement

def main():
    s = 'AAAACCCGGT'
    print(complement(s))

if __name__ == "__main__":
    main()