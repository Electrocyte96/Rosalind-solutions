#   Introduction to Random Strings
'''
Given: A DNA string s of length at most 100 bp and an array 
A containing at most 20 numbers between 0 and 1.

Return: An array B having the same length as A in which B[k] 
represents the common logarithm of the probability that a random
string constructed with the GC-content found in A[k] will match s exactly.
'''
import math

def gc_prob(a:str, b_num:list)->list:
    b = [float(x) for x in b_num]
    n = len(a)
    p_totals = []
    for b_x in b:
        result = 0.0
        p_gc = b_x/2
        p_at = (1-b_x)/2
        for i in range(n):
            if a[i] == 'G' or a[i] == 'C':
                result += math.log10(p_gc)
            else:
                result += math.log10(p_at)
        p_totals.append(round(result, 3))
    return p_totals

def main():
    a = 'ACGATACAA'
    b_num = '0.129 0.287 0.423 0.476 0.641 0.742 0.783'.split()
    p_results = gc_prob(a, b_num)
    for p in p_results:
        print(p, end=' ')

if __name__ == "__main__":
    main()