def bfs(C, R):
    dr = [0, 0, -1, 1]     #상, 하 ,좌, 우
    dc = [-1, 1, 0, 0]
    visited[C][R] = 1
    queue = [[C, R]]
    while queue:
        c, r = queue.pop(0)
        for i in range(4):
            nc = c + dc[i]
            nr = r + dr[i]
            if 0 <= nc < N and 0 <= nr < M and visited[nc][nr] == 0 and arr[nc][nr] == 1:
                queue.append([nc, nr])



N, M = map(int, input().split())        #N줄, M개

arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

ans = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and visited[i][j] == 0:
            ans.append(bfs(i, j))