def dfs(c, r, lst):
    global ans

    if len(lst) == 6:
        ans.add(tuple(lst))
        return

    for i in range(4):
        C = dc[i] + c
        R = dr[i] + r
        if 0 <= C < 5 and 0 <= R < 5:
            dfs(C, R, lst + [arr[C][R]])



dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
ans = set()
arr = [list(map(int, input().split())) for _ in range(5)]


for i in range(5):
    for j in range(5):
        dfs(i, j, [arr[i][j]])

print(len(ans))