#   Dictionaries 
'''
Given: A string s of length at most 10000 letters.

Return: The number of occurrences of each word in s, where words are separated by spaces. 
Words are case-sensitive, and the lines in the output can be in any order.
'''
def word_counter(s:str)->dict:
    word_count = {}
    for i in s.split():
        if i in word_count:
            word_count[i] += 1
        else:
            word_count[i] = 1
    return word_count

def main():
    s = 'We tried list and we tried dicts also we tried Zen'
    word_count = word_counter(s)
    for key, value in word_count.items():
        print(f"{key} {value}")

if __name__ == "__main__":
    main()