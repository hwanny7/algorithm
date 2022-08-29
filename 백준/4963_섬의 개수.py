import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(C, R):
    visited[C][R] = 1
    dr = [0, 0, -1, 1, 1, 1, -1 ,-1]
    dc = [-1, 1, 0, 0, -1, 1, 1, -1]

    for i in range(8):
        nc = C + dc[i]
        nr = R + dr[i]
        if 0 <= nc < H and 0 <= nr < W and visited[nc][nr] == 0 and arr[nc][nr] == 1:
            dfs(nc, nr)
    else:
        return 1



while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(H)]
    visited = [[0] * W for _ in range(H)]
    total = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j] == 1 and visited[i][j] == 0:
                total += dfs(i, j)

    print(total)
