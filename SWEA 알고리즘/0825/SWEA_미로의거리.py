def bfs(x, y):
    dr = [0, 0, -1, 1]     # 상, 하, 좌, 우
    dc = [-1, 1, 0, 0]
    queue = []
    visited[y][x] = 1
    queue.append([y, x])

    while queue:
        c, r = queue.pop(0)
        if arr[c][r] == 3:
            return visited[c][r] - 2
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nc < N and 0 <= nr < N and visited[nc][nr] == 0 and arr[nc][nr] != 1:
                queue.append([nc, nr])
                visited[nc][nr] = visited[c][r] + 1
    return 0


for t in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    x = y = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                x = j
                y = i
                break

    visited = [[0] * N for _ in range(N)]
    print(f'#{t}', bfs(x, y))
