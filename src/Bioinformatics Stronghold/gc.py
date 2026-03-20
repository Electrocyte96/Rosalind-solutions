#   Computing GC Content
'''
Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. 
Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; 
please see the note on absolute error below.
'''
dna_seqs = '''
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
'''.splitlines()

def fasta_to_dict(dna_seqs:str)->dict:
    seq_dict = {}
    seq=[]
    header = None
    for i in range(len(dna_seqs)):
        if dna_seqs[i].startswith('>'):
            if header:
                seq_dict[header] = ''.join(seq)
            header = dna_seqs[i][1:]
            seq = []
        else:
            seq.append(dna_seqs[i])
    if header:
        seq_dict[header] = ''.join(seq)
    return seq_dict

def gc_cont(s:str):
    gc_count=0
    n = len(s)
    for i in range(n):
        if s[i] == 'C' or s[i] == 'G':
            gc_count+=1
    return (gc_count/n)*100

def max_gc(seq_dict)->float:
    gc_max = {key: gc_cont(value) for key, value in seq_dict.items()}
    max_entry = max(gc_max, key=gc_max.get)
    max_value = gc_max[max_entry]
    return max_entry, max_value

def main():
    seq_dict = fasta_to_dict(dna_seqs)
    gc_max = max_gc(seq_dict)
    for i in gc_max:
        print(i)

if __name__ == "__main__":
    main()