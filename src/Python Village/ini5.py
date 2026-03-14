#   Working with Files
'''
Given: A file containing at most 1000 lines.

Return: A file containing all the even-numbered lines from the original file. 
Assume 1-based numbering of lines.
'''
def even_lines(route:str)->str:
    new_text = []
    f = open(f'{route}', 'r')
    text = f.readlines()
    for i in range(len(text)):
        if i%2!=0:
            new_text.append(text[i])
    return '\n'.join(new_text)

def main():
    print(even_lines('data/Python Village/ini5.txt'))

if __name__ == "__main__":
    main()