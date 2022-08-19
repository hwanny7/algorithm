n = input()
n += ' '
ans = ''

idx = 0
control = 0
start = 100,000

while True:
    if n[idx] == '<':
        control = 1
    elif n[idx] == '>':
        control = 0
    else:
        if control:
            ans += n[idx]
            idx += 1
        else:
            if n[idx] == ' ':
                n[]
                start = 100,000
            else:
                if start > idx:
                    start = idx





