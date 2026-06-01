#   Enumerating Oriented Gene Orderings
'''
Given: A positive integer n≤6.

Return: The total number of signed permutations of length n, followed by a list
of all such permutations (you may list the signed permutations in any order).
'''
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

def sign_combs(n: int) -> list[list[int]]:
    if n == 1:
        return [[1], [-1]]
    
    sign_position = []
    for i in sign_combs(n-1):
        sign_position.append([1] + i)
        sign_position.append([-1] + i)
    return sign_position

def sign_and_perms(n:int)->list:
    sign_w_perms = []
    n_list = [x for x in range(1,n+1)]
    permutations = permutation(n_list)
    for perm in permutations:
        for sign in sign_combs(n):
            sign_perm = []
            for i in range(n):
                sign_perm.append(sign[i]*perm[i])
            sign_w_perms.append(sign_perm)
    return sign_w_perms

def main():
    n = 3
    s_p = sign_and_perms(n)
    print(len(s_p))
    for i in s_p:
        print(*i)

if __name__ == "__main__":
    main()