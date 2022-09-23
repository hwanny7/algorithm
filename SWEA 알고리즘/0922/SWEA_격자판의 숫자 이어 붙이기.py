def dfs(i, j, total, K = 1):
    if K == 7:
        ans.add(total)
        return
    dc = [-1, 1, 0, 0]
    dr = [0, 0, -1, 1]
    for k in range(4):
        C = i + dc[k]
        R = j + dr[k]
        if 0 <= C < 4 and 0 <= R < 4:
            dfs(C, R, total + str(arr[C][R]), K + 1)



for t in range(1, int(input()) + 1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    ans = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, str(arr[i][j]))
    print(f'#{t}', len(set(ans)))