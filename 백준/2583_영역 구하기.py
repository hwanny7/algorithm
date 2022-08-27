def bfs(i, j):
    total = 1
    visited[i][j] = 1
    queue = [[i, j]]
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    while queue:
        c, r = queue.pop(0)
        for k in range(4):
            nc = c + dc[k]
            nr = r + dr[k]
            if 0 <= nc < C and 0 <= nr < R and visited[nc][nr] == 0 and arr[nc][nr] == 0:
                queue.append([nc, nr])
                visited[nc][nr] = 1
                total += 1
    return total


C, R, K = map(int, input().split())
arr = [[0] * (R) for _ in range(C)]
for i in range(K):
    x, y, x1, y1 = map(int, input().split())
    for i in range(y, y1):
        for j in range(x, x1):
            arr[i][j] = 1

total = []
ans = 0
visited = [[0] * (R) for _ in range(C)]
for i in range(C):
    for j in range(R):
        if arr[i][j] == 0 and visited[i][j] == 0:
            total.append(bfs(i, j))
            ans += 1
print(ans)
print(*sorted(total))