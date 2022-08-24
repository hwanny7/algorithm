def bfs(i, j, N):
    visited = [[0] * N for _ in range(N)]
    q = []
    q.append((i, j))
    visited[i][j] = 1
    while q:                    #q가 비어있지 않으면
        i, j = q.pop(0)
        if maze[i][j] == 3:      # 3번인가? (할 일)
            return 1
        for di, dj in [[0,1], [1,0], [0,-1],[-1,0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return 0        #목적지를 못 찾았을 때

T = int(input())

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

    print(f'#{tc} {bfs(sti, stj, N)}')