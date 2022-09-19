def dfs(K, cnt, lst):
    if cnt == M:
        print(*lst)
        return
    for i in range(K, N):
        lst.append(arr[i])
        dfs(i + 1, cnt + 1, lst)
        lst.pop()



N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
dfs(0, 0, [])