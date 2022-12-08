def bfs(c, r):
    global ans
    visit[c][r] = False
    Q = [[c, r]]
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    while Q:
        c, r = Q.pop(0)
        for i in range(4):
            nc = c + dc[i]
            nr = r + dr[i]
            if 0 <= nc < C and 0 <= nr < R and arr[nc][nr] and visit[nc][nr]:
                arr[nc][nr] = 0
                visit[nc][nr] = False
                Q.append([nc, nr])

    ans += 1

for t in range(1, int(input()) + 1):
    ans = 0
    R, C, cnt = map(int, input().split())
    arr = [[0] * R for _ in range(C)]
    for i in range(cnt):
        r, c = map(int, input().split())
        arr[c][r] = 1

    visit = [[True] * R for _ in range(C)]
    for i in range(C):
        for j in range(R):
            if arr[i][j] and visit[i][j]:
                bfs(i, j)

    print(ans)

