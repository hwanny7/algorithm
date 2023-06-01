dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def dfs(c, r, k):
    visited[c][r] = 1

    for i in range(4):
        nc, nr = c + dc[i], r + dr[i]
        if 0 <= nc < N and 0 <= nr < M and not visited[nc][nr] and arr[nc][nr] > k:
            dfs(nc, nr, k)




N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
K = 1
for k in range(1, 101):
    cnt = 0
    visited = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] > k and not visited[i][j]:
                dfs(i, j, k)
                cnt += 1
    if ans < cnt:
        ans = cnt
        K = k

print(ans, K)

