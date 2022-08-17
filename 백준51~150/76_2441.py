
n = int(input())

for i in range(n, 0, -1):
    s = ''
    s += ' ' * (n-i) + '*' * i
    print(s)
