def find(x, lst = [1]):
    print(lst)

    for i in path[x]:
        if visit[i]:
            visit[i] = False
            find(i, lst + [i])
            visit[i] = True

N = int(input())
pop = list(map(int, input().split()))

path = [[] for _ in range(N + 1)]
visit = [True] * (N + 1)
for idx in range(1, N + 1):
    adj = list(map(int, input().split()))
    for j in range(1, adj[0] + 1):
        path[idx].append(adj[j])

visit[1] = False
find(1)
