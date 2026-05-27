#   Perfect Matchings and RNA Secondary Structures
'''
Given: An RNA string s of length at most 80 bp having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.

Return: The total possible number of perfect matchings of basepair edges in the bonding graph of s.
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

def facts(x:int)->int:
    if x == 0 or x == 1:
        return 1
    else:
        return x * facts(x-1)

def count_matchings(seq:str)->str:
    base_count = {}
    for base in seq:
        if base in base_count:
            base_count[base] += 1
        else:
            base_count[base] = 1 
    
    if base_count['A'] == base_count['U']:
        a_factorial = facts(base_count['A'])
    else:
        return None
    if base_count['C'] == base_count['G']:
        c_factorial = facts(base_count['C'])
    else:
        return None
    
    return a_factorial * c_factorial

def main():
    seq_fas = '''
>Rosalind_23
AGCUAGUCAU
'''.splitlines()
    seq_dict = fasta_to_dict(seq_fas)
    seq_l = list(seq_dict.values())
    print(count_matchings(seq_l[0]))

if __name__ == "__main__":
    main()