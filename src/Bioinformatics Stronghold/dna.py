#   A Rapid Introduction to Molecular Biology
'''
Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of 
times that the symbols 'A', 'C', 'G', and 'T' occur in s.
'''
def nt_count(s:str)->dict:
    nt_count = {'A':0, 'C':0, 'G':0, 'T':0}
    for i in s:
        nt_count[i]+=1
    return nt_count

def main():
    s = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
    nt_dict = nt_count(s)
    print(*list(nt_dict.values()), sep=' ')

if __name__ == "__main__":
    main()