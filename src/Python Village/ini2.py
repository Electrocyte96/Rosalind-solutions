#   Variables and Some Arithmetic 
'''
Problem 
Given: Two positive integers a and b, each less than 1000.

Return: The integer corresponding to the square of the hypotenuse 
of the right triangle whose legs have lengths a and b.
'''
def hypo(a:int, b:int)->int:
    return (a**2) + (b**2)

def main():
    print(hypo(3,5))

if __name__ == "__main__":
    main()