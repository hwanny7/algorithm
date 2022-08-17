
n = int(input())
k = int(input())

arr = [[0] * n for _ in range(n)]

dr = [0, 1, 0, -1]# 하, 우, 상, 좌
dc = [1, 0, -1, 0]

r = 0
c = -1
j = 0
box = 0 # k 좌표값 저장

for i in range(n*n, 0, -1):
    if 0 <= c + dc[j % 4] < n and 0 <= r + dr[j % 4] < n and arr[c + dc[j % 4]][r + dr[j % 4]] == 0:
        arr[c + dc[j % 4]][r + dr[j % 4]] = i
        r = r + dr[j % 4]
        c = c + dc[j % 4]

    else:
        j += 1
        arr[c + dc[j % 4]][r + dr[j % 4]] = i
        r = r + dr[j % 4]
        c = c + dc[j % 4]

    if i == k:
        box = (c + 1, r + 1)

for j in arr:
    print(*j)
print(*box)


