#   Enumerating k-mers Lexicographically
'''
Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).

Return: All strings of length n that can be formed from the alphabet, ordered lexicographically 
(use the standard order of symbols in the English alphabet).
'''
def enum_kmers(keys:list, k:int)->list:
    if k == 1:
        return keys
    final_perms = []
    for key in keys:
        subkeys = enum_kmers(keys, k-1)
        for subkey in subkeys:
            final_perms.append(key + subkey)
    return final_perms

def main():
    keys = ['A', 'C', 'G', 'T']
    k = 2
    kmers = enum_kmers(keys, k)
    for i in kmers:
        print(i)

if __name__ == "__main__":
    main()