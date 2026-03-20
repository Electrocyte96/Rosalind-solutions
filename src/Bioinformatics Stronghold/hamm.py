#   Counting Point Mutations
'''
Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).
'''
def hamming(s:str, t:str):
    count = 0
    if len(s) == len(t):
        for nt in range(len(s)):
            if s[nt] != t[nt]:
                count+=1
    return count

def main():
    s='GAGCCTACTAACGGGAT'
    t='CATCGTAATGACGGCCT'
    print(hamming(s,t))

if __name__ == "__main__":
    main()