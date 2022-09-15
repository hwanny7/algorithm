def dfs(v, deep):
    visited[v] = deep
    for i in V[v]:
        if not visited[i]:
            dfs(i, deep + 1)

# def dfs(v):
#     global max
#     visited[v] = 1
#     queue = []
#     queue.append(v)
#     while queue:
#         n = queue.pop(0)
#         for i in V[n]:
#             if visited[i] == 0:
#                 queue.append(i)
#                 visited[i] = visited[n] + 1
#                 max = visited[i]


for t in range(1, 11):
    N, start = map(int, input().split())
    arr = list(map(int, input().split()))
    V = [[] for _ in range(101)]
    ans = []
    for i in range(0, N, 2):
        V[arr[i]].append(arr[i + 1])
    visited = [0] * 101
    max = 0
    dfs(start, 1)
    # dfs(start)
    print(visited)

    for i in range(len(visited) - 1, -1, -1):
        if visited[i] == max:
            print(i)
            break
