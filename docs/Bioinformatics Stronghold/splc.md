for i in range(10):
    if i == 7:
        i += i*2
    print(i)
print('---------------------------------')
i = 0
while i < 25:
    if i == 7:
        i += i*2
        print(i)
    else:
        i += 1
        print(i)

s_1 = s.replace(sub_s[0], '').replace(sub_s[1], '')