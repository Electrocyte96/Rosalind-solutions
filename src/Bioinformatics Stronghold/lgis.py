#   Longest Increasing Subsequence
'''
Given: A positive integer n≤10000 followed by a permutation π of length n.

Return: A longest increasing subsequence of π, followed by a longest decreasing subsequence of π.
'''
def longest_increasing(perm:list, n:int)->list:
    longs = [1]*n
    padres = [-1] * n 
    for i in range(n):
        for j in range(i):
            if perm[j] < perm[i]: 
                if longs[j] + 1 > longs[i]:
                    longs[i] = longs[j] + 1
                    padres[i] = j
    idx = longs.index(max(longs))
    lis = []
    while idx != -1:
        lis.append(perm[idx])
        idx = padres[idx]
    return lis[::-1]

def longest_decreasing(perm:list, n:int)->list:
    longs = [1]*n
    padres = [-1] * n 
    for i in range(n):
        for j in range(i):
            if perm[j] > perm[i]: 
                if longs[j] + 1 > longs[i]:
                    longs[i] = longs[j] + 1
                    padres[i] = j
    idx = longs.index(max(longs))
    lis = []
    while idx != -1:
        lis.append(perm[idx])
        idx = padres[idx]
    return lis[::-1]

def main():
    perm = '''
5 1 4 2 3
'''.split()
    perm = [int(x) for x in perm]
    n = 5
    increasing = longest_increasing(perm, n)
    decreasing = longest_decreasing(perm, n)
    for i in increasing:
        print(i, end=' ')
    print()
    for i in decreasing:
        print(i, end=' ')

if __name__ == "__main__":
    main()