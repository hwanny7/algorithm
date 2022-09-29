def find():
    visit = [0] * (V + 1)
    value = [10000000] * (V + 1)
    value[0] = 0

    for j in range(V):
        minV = 10000000
        idx = 0
        for i in range(V + 1):
            if visit[i] == 0 and minV > value[i]:
                minV = value[i]
                idx = i

        visit[idx] = 1

        for e, w in path[idx]:
            if visit[e] == 0:
                value[e] = min(value[e], w)

    print(f'#{t}', sum(value))

for t in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    path = [[] for _ in range(V + 1)]

    for i in range(E):
        s, e, w = map(int, input().split())
        path[s].append((e, w))
        path[e].append((s, w))
    find()

