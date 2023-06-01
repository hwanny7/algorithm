dc = [-1, 1, 0, 0]
dr = [0, 0, -1, 1]

def dfs(c, r):
    global cnt
    cnt += 1
    visited[c][r] = 1

    for i in range(4):
        nc , nr = c + dc[i], r + dr[i]
        if 0 <= nc < N and 0 <= nr < N and arr[nc][nr] and not visited[nc][nr]:
            dfs(nc, nr)





N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]

total = 0
cnt = 0
ans = []

for i in range(N):
    for j in range(N):
        if arr[i][j] and not visited[i][j]:
            dfs(i, j)
            total += 1
            ans.append(cnt)
            cnt = 0

print(total)
for num in sorted(ans):
    print(num)