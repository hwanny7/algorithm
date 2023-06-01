dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def dfs(c, r, num):
    global total


    total += 1
    visited[c][r] = 1

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and not visited[nc][nr] and arr[nc][nr] == num:
            dfs(nc, nr, num)



N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
bloc = 0
total = 0
ans = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j, arr[i][j])
            if total >= 4:
                bloc += 1
            ans = max(ans, total)
            total = 0

print(bloc, ans)