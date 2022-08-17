
for t in range(int(input())):
    n = int(input())
    total = 0
    X = 0
    for i in range(n):
        x, y = map(float, input().split())
        total += x * y
        X += x
    print(int(X) , round(total / X, 1))