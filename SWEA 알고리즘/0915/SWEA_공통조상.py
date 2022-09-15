def Tree(v):
    if not v:
        return 0

    total = 0
    for i in track[v]:
        total += Tree(i)

    return total + 1


for t in range(1, int(input()) + 1):
    V, E, P1, P2 = map(int, input().split())
    track = [[] for _ in range(V + 1)]
    parent = [0] * (V + 1)
    arr = list(map(int, input().split()))
    for i in range(0, E * 2, 2):
        track[arr[i]].append(arr[i + 1])
        parent[arr[i + 1]] = arr[i]

    lst = [0] * (V + 1)
    ans = 0
    while not ans:
        lst[parent[P1]] += 1
        lst[parent[P2]] += 1
        if parent[P1] != 0 and lst[parent[P1]] == 2:
            ans = parent[P1]
        elif parent[P2] != 0 and lst[parent[P2]] == 2:
            ans = parent[P2]
        P1 = parent[P1]
        P2 = parent[P2]

    print(f'#{t}', ans, Tree(ans))

