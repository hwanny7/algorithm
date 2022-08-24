def dfs(i, j, N):
    if maze[i][j] == 3:
        return
    else:
        visited[i][j] = 1
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i + di, j + dj
            if maze[ni][nj] != 1 and visited[ni][nj] == 0:      # 벽으로 둘러 쌓인 미로라서 범위 검색을 할 필요가 없음
                dfs(ni, nj, N)






for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sti = -1
    stj = -1

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sti, stj = i, j     #시작 좌표
                break
        if sti != -1:
            break
    visited = [[0] * N for _ in range(N)]
    print(f'#{tc} {bfs(sti, stj, N)}')