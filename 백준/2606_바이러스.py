def dfs(x):
    global total
    visited[x] = 1
    total += 1
    for i in V[x]:
        if visited[i] == 0:
            dfs(i)
    return


N = int(input())
M = int(input())
V = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
total = 0
for i in range(M):
    f, l = map(int, input().split())
    V[f].append(l)
    V[l].append(f)

dfs(1)
print(total - 1)


