

n = int(input())

for i in list(range(2*n-1, 0, -2))+list(range(3, 2*n, 2)):
    print(' ' * (abs((i - (2*n-1))) // 2) + '*' * i)
