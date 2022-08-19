
n = int(input())

arr = [[0] * 1001 for _ in range(1001)]
num = 1
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for c in range(y1, y1+y2):
        for r in range(x1, x1+x2):
            arr[c][r] = num
    num += 1

count = 0

for k in range(1, num):
    count = 0
    for i in arr:
        for j in i:
            if j == k:
                count += 1
    print(count)