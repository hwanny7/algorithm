

n = int(input())

for i in list(range(1, n+1)) + list(range(n-1, 0, -1)):
    print(' ' * (n-i)+'*' * i)
