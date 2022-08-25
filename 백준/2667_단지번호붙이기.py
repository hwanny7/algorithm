def bfs(c, r):
    dr = [0, 0, -1, 1]     #상, 하, 좌, 우
    dc = [-1, 1, 0, 0]
    # visited = [[0] * N for _ in range(N)]
    # vistied[c][r] = 1
    queue = [[c, r]]
    arr[c][r] = 0
    cnt = 1
    while queue:
        C, R = queue.pop()
        for i in range(4):
            nc = C + dc[i]
            nr = R + dr[i]
            if 0 <= nc < N and 0 <= nr < N and arr[nc][nr] != 0:
                queue.append([nc, nr])
                cnt += 1
                arr[nc][nr] = 0
    return cnt



N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
ans = []
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            ans.append(bfs(i, j))

print(len(ans))
for i in sorted(ans):
    print(i)


