
str = input()
str += ' '
ans = ''
control = 0
start = 100000000

for i in range(len(str)):
    if control == 1:        # 태그일 때
        if str[i] == '>':
            ans += str[i]
            control = 0
        else:
            ans += str[i]

    else:
        if str[i] == '<':
            if start != 100000000:
                ans += str[start:i][::-1]
                start = 100000000
            ans += str[i]
            control = 1
        elif str[i] == ' ':
            ans += str[start:i][::-1] + ' '
            start = 100000000
        elif start > i:
            start = i

print(ans.rstrip())
