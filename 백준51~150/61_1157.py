

n = input()
lst = [0] * 26

for i in n:
    lst[ord(i.upper())-65] += 1



if sorted(lst, reverse =True )[0] == sorted(lst, reverse= True)[1]:
    print('?')
else:
    max = 0
    for i in range(26):
        if lst[max] < lst[i]:
            max = i
    print(chr(max+65).upper())