
#
s = list(input())

answer = ''

for i in s:
    if i.islower():
        if ord(i)+13 > 122:
            answer += chr((ord(i)+13) % 122 + 96)
        else:
            answer += chr(ord(i)+ 13)
    elif i.isupper():
        if ord(i)+13 > 90:
            answer += chr((ord(i) + 13) % 90 + 64)
        else:
            answer += chr(ord(i) + 13)
    else:
        answer += i
print(answer)
