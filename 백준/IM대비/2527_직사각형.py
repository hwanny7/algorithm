
x, y, x1, y1, r, c, r1, c1 = map(int, input().split())

arr = [[0] * (max(x1, r1) + 1) for _ in range(max(y1, c1) + 1)]
print(max(x1, r1) + 1, max(y1, c1) + 1)

for i in range(x, x1 + 1):
    for j in range(y, y1 + 1):
        arr[j][i] += 1

for i in range(r, r1 + 1):
    for j in range(c, c1 + 1):
        arr[j][i] += 1

for i in arr:
    print(*i)