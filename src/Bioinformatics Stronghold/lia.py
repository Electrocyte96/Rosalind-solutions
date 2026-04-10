#   Independent Alleles
'''
Given: Two positive integers k (k≤7) and N (N≤2k). In this problem, we begin with Tom,
who in the 0th generation has genotype Aa Bb. Tom has two children in the 1st generation,
each of whom has two children, and so on. Each organism always mates with an organism having genotype Aa Bb.

Return: The probability that at least N Aa Bb organisms will belong to the k-th generation 
of Tom's family tree (don't count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors.
'''
def facts(x:int)->int:
    if x == 0 or x == 1:
        return 1
    else:
        return x * facts(x-1)

def combi(n:int, x:int)->float:
    return (facts(n))/(facts(x)*(facts(n-x)))

def het_binom(k:int, n:int)->float:
    k = 2**k
    p_het = 0.25
    q = 1 - p_het
    p_total = 0.0
    for i in range(n, k+1):
        p_total += combi(k, i) * p_het**i * q**(k-i)
    return p_total

def main():
    k = 2
    n = 1
    print(f"{het_binom(k,n):.3f}")

if __name__ == "__main__":
    main()