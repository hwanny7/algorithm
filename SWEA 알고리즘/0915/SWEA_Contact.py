def dfs(v):
    global final
    visited[v] = 1
    queue = []
    queue.append(v)
    while queue:
        n = queue.pop(0)
        for i in V[n]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[n] + 1
                ans[visited[i]].append(i)
                final = visited[i]


for t in range(1, 11):
    N, start = map(int, input().split())
    arr = list(map(int, input().split()))
    V = [[] for _ in range(101)]
    visited = [0] * 101
    final = 0

    for i in range(0, N, 2):
        V[arr[i]].append(arr[i + 1])

    ans = [[] for _ in range(101)]
    dfs(start)
    print(f'#{t}',max(ans[final]))


