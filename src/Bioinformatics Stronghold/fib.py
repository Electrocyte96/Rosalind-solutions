#   Rabbits and Recurrence Relations
'''
Given: Positive integers n≤40 and k≤5.

Return: The total number of rabbit pairs that will be present after n months, 
if we begin with 1 pair and in each generation, every pair of reproduction-age 
rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
'''
def wabbits(n:int, k:int)->int:
    a = 1
    b = 1
    if n<=2:
        return 1
    for i in range(2, n):
        aux = b + k * a
        a = b
        b = aux
    return b

def main():
    print(wabbits(5,3))

if __name__ == "__main__":
    main()