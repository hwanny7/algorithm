def dfs(c, r):
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    visited[c][r] = 1
    if arr[c][r] == 3:
        return 1

    for i in range(4):
        nc = c + dc[i]
        nr = r + dr[i]
        if 0 <= nc < 16 and 0 <= nr < 16 and arr[nc][nr] != 1 and visited[nc][nr] != 1:
            result = dfs(nc, nr)
            if result == 1:
                return 1

    return 0


for t in range(1, 11):
    T = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]

    print(f'#{t}', dfs(1, 1))

