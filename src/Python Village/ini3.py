#   Strings and Lists
'''
Given: A string s of length at most 200 letters and four integers a, b, c and d.

Return: The slice of this string from indices a through b and c through d 
(with space in between), inclusively. In other words, we should include 
elements s[b] and s[d] in our slice.
'''
def slices(s:str, a:int, b:int, c:int, d:int)->str:
    return s[a:b+1] + ' ' + s[c:d+1] 


def main():
    test = 'HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.'
    a, b, c, d = 22, 27, 97, 102
    print(slices(test, a, b, c, d))

if __name__ == "__main__":
    main()