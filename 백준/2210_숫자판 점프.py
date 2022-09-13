def dfs(D):
    if D == 6:
        print(*ans)
        return
    for i in arr:
        ans[D] = i
        dfs(D + 1)


set1 = set()
arr = [list(map(int, input().split)) for _ in range(5)]
for i in range(5):
    for j in range(5):
