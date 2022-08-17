n = int(input())

for i in list(range(2, n*2+1, 2)) + list(range(n*2-2, 1, -2)):
    print('*' * (i // 2) + ' ' * (n * 2 - i) + '*' * (i // 2))