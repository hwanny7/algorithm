def bfs(x, y):
    dr = [0, -1, 1]     #하, 좌, 우
    dc = [1, 0, 0]
    visited[x][y] = [1, 1]
    queue = [[x, y, 1]]
    while queue:        # visited 먼저 방문하는 놈 때문에 우선순위 문제가 생겨남
        print(queue)
        c, r, count = queue.pop(0)
        for i in range(3):
            C = c + dc[i]
            R = r + dr[i]
            if 0 <= C < N and 0 <= R < M:
                if visited[C][R] == 0:
                    if arr[C][R] == 1:
                        if count == 1:
                            queue.append([C, R, 0])
                            visited[C][R] = visited[c][r] + 1
                            cnt[C][R] = count - 1


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
cnt = [[5] * M for _ in range(N)]
bfs(0, 0)

if visited[N-1][M -1]:
    print(visited[N-1][M -1])
else:
    print(-1)

for i in visited:
    print(*i)