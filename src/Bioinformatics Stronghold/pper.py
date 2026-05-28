#   Partial Permutations
'''
Given: Positive integers n and k such that 100≥n>0 and 10≥k>0.

Return: The total number of partial permutations P(n,k), modulo 1,000,000.
'''
def facts(x:int)->int:
    if x == 0 or x == 1:
        return 1
    else:
        return x * facts(x-1)

def partial_perm(n:int, k:int)->int:
    return int(facts(n)/facts(n-k)%1000000)

def main():
    n, k = 94, 8
    print(partial_perm(n, k))

if __name__ == "__main__":
    main()