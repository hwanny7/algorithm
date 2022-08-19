
n = int(input())
m = 101
arr = [[0] * m for _ in range(m)]
for i in range(n):
    x, y = map(int, input().split())  # x는 가로, y는 세로
    for c in range(x, x+10):
        for r in range(y, y+10):
            arr[c][r] += 1

dr = [0, 0, -1, 1]     #상, 하, 좌, 우
dc = [1, -1, 0, 0]
count = 0
arr2 = [[0] * 30 for _ in range(30)]
for i in range(m):
    for j in range(m):
        if arr[i][j] != 0:
            for k in range(4):
                if 0 <= i + dc[k] < m and 0 <= j + dr[k] < m and arr[i + dc[k]][j + dr[k]] == 0:
                    count += 1

print(count)




