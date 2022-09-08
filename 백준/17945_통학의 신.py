A, B = map(int, input().split())

for x in range(-1000, 1001, 1):
    if (-x)**2 + 2*A*x + B == 0:
        print(x, end = ' ')