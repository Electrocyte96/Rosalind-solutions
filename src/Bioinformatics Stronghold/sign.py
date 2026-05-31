#   Enumerating Oriented Gene Orderings
'''
Given: A positive integer n≤6.

Return: The total number of signed permutations of length n, followed by a list
of all such permutations (you may list the signed permutations in any order).
'''

def sign_combos(n: int) -> list[list[int]]:
    if n == 1:
        return [[1], [-1]]
    
    result = []
    for remainder in sign_combos(n-1):
        print('sign_combos=',sign_combos(n-1), 'n=',n-1)
        print('remainder=', remainder)
        result.append([1] + remainder)
        #print('pos_one', '[1]', 'remainder', remainder)
        result.append([-1] + remainder)
        #print('neg_one', '[-1]', 'remainder', remainder)
        #print('when n=',n-1,'result=', result)
    return result


def main():
    n = 2
    print(sign_combos(n))

if __name__ == "__main__":
    main()