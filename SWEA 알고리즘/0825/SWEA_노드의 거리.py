def bfs(S, E):
    visited[S] = 1
    queue = [S]

    while queue:
        v = queue.pop(0)
        for i in G[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[v] + 1
                if i == E:
                    return visited[i] - 1
    return 0

for t in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]

    for i in range(E):
        s, e = map(int, input().split())
        G[s].append(e)
        G[e].append(s)

    Start, End  = map(int, input().split())
    visited = [0] * (V + 1)
    print(f'#{t}', bfs(Start, End))


