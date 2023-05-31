def dfs(vertex):
    global ans
    for v in connected[vertex]:
        if not visited[v]:
            visited[v] = True
            ans += 1
            print(v)
            dfs(v)


V, E = map(int, input().split(" "))
connected = [[] for _ in range(V + 1)]

for i in range(E):
    start, end = map(int, input().split(" "))
    connected[start].append(end)
    connected[end].append(start)

ans = 0
visited = [False for _ in range(V + 1)]

dfs(1)
print(ans)
