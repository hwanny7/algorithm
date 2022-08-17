
m, n = map(int, input().split())

arr = [[0] * n for _ in range(m)]

dr = [1, 0, -1, 0]   #우, 하, 좌, 상
dc = [0, 1, 0, -1]

r = -1
c = 0
j = 0
count = 0

for i in range(1, m*n+1):
    if 0 <= c + dc[j % 4] < m and 0 <= r + dr[j % 4] < n and arr[c + dc[j % 4]][r + dr[j % 4]] == 0:
        arr[c + dc[j % 4]][r + dr[j % 4]] = i
        r = r + dr[j % 4]
        c = c + dc[j % 4]

    else:
        j += 1
        count += 1
        arr[c + dc[j % 4]][r + dr[j % 4]] = i
        r = r + dr[j % 4]
        c = c + dc[j % 4]

print(count)