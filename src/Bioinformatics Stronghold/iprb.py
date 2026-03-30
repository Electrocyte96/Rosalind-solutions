#   Mendel's First Law
'''
Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: 
k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual 
possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two
organisms can mate
'''
def p_dominant(k:int, m:int, n:int)->float:
    total = k+m+n
    p_AaxAa = 0.25
    p_Aaxaa = 0.50
    p_aaxaa = 1

    p_mxm = (m/total) * ((m-1)/(total-1)) * p_AaxAa
    p_mxn_p_nxm = 2 * ((m/total) * ((n)/(total-1)) * p_Aaxaa)
    p_nxn = (n/total) * ((n-1)/(total-1)) * p_aaxaa

    return 1 - (p_mxm + p_mxn_p_nxm + p_nxn) 
def main():
    k, m, n = 2 ,2, 2
    prob = p_dominant(k,m,n)
    print(f"{prob:.5f}")

if __name__ == "__main__":
    main()
