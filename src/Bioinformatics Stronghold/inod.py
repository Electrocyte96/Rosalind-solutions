#   Counting Phylogenetic Ancestors
'''
Given: A positive integer n (3≤n≤10000).

Return: The number of internal nodes of any unrooted binary tree having n leaves
'''
def unrooted_nodes(n:int)->int:
    return n-2

def main():
    n = 6162
    print(unrooted_nodes(n))

if __name__ == "__main__":
    main()