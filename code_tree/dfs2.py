def dfs(x, y):
    if (x, y) == (M - 1, N - 1):
        return 1

    visited[y][x] = True
    dxs, dys = [1, 0] , [0, 1]
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx , y + dy
        if 0 <= new_x < M and 0 <= new_y < N and arr[new_y][new_x] and not visited[new_y][new_x]:
            next = dfs(new_x, new_y)
            if next:
                return 1

    else:
        return 0


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]


visited = [[False for _ in range(M)] for _ in range(N)]

print(dfs(0, 0))

