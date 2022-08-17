

for i in range(int(input())):
    x, y = map(int, input().split())
    lst = [0] * y
    count = 0
    for i in range(x):
        n = int(input())
        if lst[n-1] == 0:
            lst[n-1] += 1
        else:
            count += 1
    print(count)
