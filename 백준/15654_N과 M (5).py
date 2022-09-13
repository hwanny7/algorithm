def dfs(ans, D):
    if D == M:
        print(*ans)
    for i in range(N):
        if arr[i] == 0:
            continue
        temp = arr[i]
        ans.append(arr[i])
        arr[i] = 0
        dfs(ans, D + 1)
        arr[i] = temp
        ans.pop()


N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
dfs([], 0)