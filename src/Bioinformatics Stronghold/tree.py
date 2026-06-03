#   Completing a Tree
'''
Given: A positive integer n (n≤1000) and an adjacency list corresponding to a graph on n nodes that contains no cycles.

Return: The minimum number of edges that can be added to the graph to produce a tree.
'''
def tree_edges(data:list)->int:
    nodes = int(data.pop(0))
    return (nodes - len(data))-1

def main():
    data = '''10
1 2
2 8
4 10
5 9
6 10
7 9
'''.splitlines()
    print(tree_edges(data))

if __name__ == "__main__":
    main()