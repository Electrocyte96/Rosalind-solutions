#   Conditions and Loops
'''
Given: Two positive integers a and b (a<b<10000).

Return: The sum of all odd integers from a through b, inclusively.
'''
def sum_odds(a:int ,b:int)->int:
    x=0
    for i in range(a, b+1):
        if i % 2 != 0:
            x+=i
    return x

def main():
    print(sum_odds(100, 200))

if __name__ == "__main__":
    main()