

C, R, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(C)]

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
Q = []
for i in range(C):
    for j in range(R):
        if arr[i][j] > 0:
            Q.append([i, j])

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
while Q:
    c, r = Q.pop(0)
    num = int(arr[c][r] / 5)
    cnt = 0
    for i in range(4):
        nc = c + dc[i]
        nr = r + dr[i]
        if 0 <= nc < C and 0 <= nr < R and arr[nc][nr] != -1:
            arr[nc][nr] += num
            cnt += 1
    arr[c][r] -= num * cnt

for i in arr:
    print(*i)