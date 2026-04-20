#   Enumerating Gene Orders
'''
Given: A positive integer n≤7.

Return: The total number of permutations of length n, 
followed by a list of all such permutations (in any order).
'''
def facts(x:int)->int:
    if x == 0 or x == 1:
        return 1
    else:
        return x * facts(x-1)

def permutation(elements:list)->list:
    if len(elements) == 1:
        return [elements]
    result = []
    for i in range(len(elements)):
        first_symbol = elements[i]
        remaining = elements[:i] + elements[i+1:]
        subperms = permutation(remaining)
        for rest in subperms:
            result.append([first_symbol] + rest)
    return result

def main():
    n = 3
    n_list = [x for x in range(1,n+1)]
    perm_n = permutation(n_list)
    print(facts(n))
    for i in perm_n:
        print(*i)

if __name__ == "__main__":
    main()


