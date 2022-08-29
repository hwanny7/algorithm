import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x):
    visited[x] = 1

    for i in V[x]:
        if visited[i] == 0:
            dfs(i)
    else:
        return 1

N, M = map(int, input().split())
V = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for i in range(M):
    start, end = map(int, input().split())
    V[start].append(end)
    V[end].append(start)

total = 0
for i in range(1, N + 1):
    if visited[i] == 0:
        total += dfs(i)

print(total)