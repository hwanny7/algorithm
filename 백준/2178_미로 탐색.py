def dfs():
    visited[0][0] = 1
    queue = [[0, 0]]
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    while queue:
        c, r = queue.pop(0)
        for i in range(4):
            nc = c + dc[i]
            nr = r + dr[i]
            if 0 <= nc < C and 0 <= nr < R and visited[nc][nr] == 0 and arr[nc][nr] == 1:
                queue.append([nc, nr])
                visited[nc][nr] = visited[c][r] + 1


C, R = map(int, input().split())

visited = [[0] * R for _ in range(C)]
arr = [list(map(int, input())) for _ in range(C)]
dfs()
print(visited[C - 1][R - 1])