def dfs(V):
    visited[V] = 1
    print(V, end = ' ')
    for i in path[V]:
        if not visited[i]:
            dfs(i)



def bfs(V):
    visited = [0] * (N + 1)
    visited[V] = 1
    queue = [V]
    while queue:
        V = queue.pop(0)
        print(V, end= ' ')
        for i in path[V]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1


N, M, V = map(int, input().split())

path = [[] for _ in range(N + 1)]
for i in range(M):
    start, end = map(int, input().split())
    path[start].append(end)
    path[end].append(start)

for j in range(1, N + 1):
    path[j].sort()

visited = [0] * (N + 1)
dfs(V)
print()
bfs(V)


