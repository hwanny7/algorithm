
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
high = [[] for _ in range(101)]

low_high = 1000
max_high = 0
for i in range(N):
    for j in range(N):
        high[arr[i][j]].append((i, j))
        if max_high < arr[i][j]:
            max_high = arr[i][j]
        elif low_high > arr[i][j]:
            low_high = arr[i][j]

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
ans = 1
for i in range(low_high, max_high):
    for x, y in high[i]:
        arr[x][y] = 0
    visit = [[True] * N for _ in range(N)]
    cnt = 0
    for col in range(N):
        for row in range(N):
            if arr[col][row] and visit[col][row]:
                cnt += 1
                q = [(col, row)]
                visit[col][row] = False
                while q:
                    c, r = q.pop(0)
                    for i in range(4):
                        nc = c + dc[i]
                        nr = r + dr[i]
                        if 0 <= nc < N and 0 <= nr < N and arr[nc][nr] and visit[nc][nr]:
                            visit[nc][nr] = False
                            q.append((nc, nr))
    if ans < cnt:
        ans = cnt

print(ans)