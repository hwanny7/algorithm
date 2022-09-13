def dfs(S,D, start):
    if D == 6:
        print(*S)
        return
    for i in range(start, N):
        if visited[i]:
            continue
        S.append(arr[i])
        dfs(S, D + 1, i + 1)
        visited[i] = 0
        S.pop()

while True:
    arr = list(map(int, input().split()))
    N = arr[0]
    if N == 0:
        break
    arr = arr[1::]
    visited = [0] * N
    dfs([], 0, 0)
    print()