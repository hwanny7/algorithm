

n = input()+'+'
total = 0
temp = ''
control = 0
for i in range(len(n)):
    if n[i] == '-':
        if control == 0:
            total += int(temp)
            temp = ''
            control = 1
        else:
            total -= int(temp)
            temp = ''

    elif n[i] == '+':
        if control > 0:
            total -= int(temp)
            temp = ''
        else:
            total += int(temp)
            temp = ''
    else:
        temp += n[i]

print(total)





# +나 부호가 없을 경우 total 추가
# -일 경우 그 뒤로 이어지는 건 계속해서 -

