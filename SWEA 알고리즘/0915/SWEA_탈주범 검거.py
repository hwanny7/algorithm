def bfs(C, R):
    visited = [[0] * M for _ in range(N)]
    queue = [[C, R]]
    visited[C][R] = 1
    while queue


for t in range(1, int(input()) + 1):
    N, M, C, R, T = map(int, input().split()) # N 세로, M가로
    arr = [list(map(int, input().split())) for _ in range(N)]
    bfs(C, R)
    dr = [,[0, 0],[-1, 1]]
    dc = [,[-1, 1],[0, 0]]