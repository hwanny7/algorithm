
def dfs(K):
    if K == M:
        print(*arr)
        return
    else:
        for i in range(1, N + 1):
            arr[K] = i
            dfs(K + 1)


N, M = map(int, input().split())
arr = [0] * M
dfs(0)

