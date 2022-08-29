def bfs(i, j, a):
    visited[i][j] = 1
    queue = [[i, j]]
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    total = 1
    while queue:
        c, r = queue.pop(0)
        for i in range(4):
            nc = c + dc[i]
            nr = r + dr[i]
            if 0 <= nc < C and 0 <= nr < R and visited[nc][nr] == 0 and arr[nc][nr] == a:
                visited[nc][nr] = 1
                queue.append([nc, nr])
                total += 1
    return total ** 2




R, C = map(int, input().split())

arr = [list(input()) for _ in range(C)]
visited = [[0] * R for _ in range(C)]

total_W = 0
total_B = 0
for i in range(C):
    for j in range(R):
        if visited[i][j] == 0:
            if arr[i][j] == 'W':
                total_W += bfs(i, j, arr[i][j])
            elif arr[i][j] == 'B':
                total_B += bfs(i, j, arr[i][j])

print(total_W, total_B)

