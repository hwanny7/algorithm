def dfs(S, cnt):
    if S == end:
        return cnt
    visited[S] = 1
    for i in dis[S]:
        if not visited[i]:
            verify = dfs(i, cnt + 1)
            if verify > -1:
                return verify
    else:
        return -1


N = int(input())
start, end = map(int, input().split())
V = int(input())
dis = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for i in range(V):
    S, E = map(int, input().split())
    dis[S].append(E)
    dis[E].append(S)

print(dfs(start, 0))