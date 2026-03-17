#   Transcribing DNA into RNA
'''
Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.
'''
def to_rna(t:str)->str:
    return t.replace('T', 'U') 

def main():
    t = 'GATGGAACTTGACTACGTAAATT'
    print(to_rna(t))

if __name__ == "__main__":
    main()