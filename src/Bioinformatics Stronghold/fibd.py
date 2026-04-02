#   Mortal Fibonacci Rabbits
'''
Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the 
n-th month if all rabbits live for m months.
'''
def mortal_wabbits(n:int, m:int)->int:
    edad = [1] + [0]*(m-1)
    for i in range(1, n):
        nuevos = sum(edad[1:])
        edad = [nuevos] + edad[:-1]
    return sum(edad)

def main():
    print(mortal_wabbits(89, 16))

if __name__ == "__main__":
    main()