def dfs(x, y):
    arr[y][x] = 0
    queue = [[y, x]]
    while queue:
        c, r = queue.pop(0)
        dr = [0, 0, -1, 1, 1, 1, -1, -1]
        dc = [-1, 1, 0, 0, -1, 1, 1, -1]
        for i in range(8):
            nc = c + dc[i]
            nr = r + dr[i]
            if 0 <= nc < C and 0 <= nr < R and arr[nc][nr] == 1:
                queue.append([nc, nr])
                arr[nc][nr] = 0
    return 1

C, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(C)]

total = 0
for i in range(C):
    for j in range(R):
        if arr[i][j] == 1:
            total += dfs(j, i)

print(total)