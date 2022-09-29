def find(x):
    if V[x] == x:
        return x
    return find(V[x])


for t in range(1, int(input()) + 1):
    people, paper = map(int, input().split())
    arr = list(map(int, input().split()))
    V = [i for i in range(people + 1)]
    for i in range(0, paper * 2, 2):
        V[find(arr[i + 1])] = V[find(arr[i])]
    ans = 0
    for j in range(1, people + 1):
        if j == V[j]:
            ans += 1
    print(V)
    print(f'#{t}', ans)


# def dfs(x):
#     visit[x] = 1
#     for i in V[x]:
#         if not visit[i]:
#             dfs(i)
#
# for t in range(1, int(input()) + 1):
#     people, paper = map(int, input().split())
#     arr = list(map(int, input().split()))
#     V = [[] for i in range(people + 1)]
#     for i in range(0, paper * 2, 2):
#         V[arr[i]].append(arr[i + 1])
#         V[arr[i + 1]].append(arr[i])
#     visit = [0] * (people + 1)
#     cnt = 0
#     for i in range(1, people + 1):
#         if not visit[i]:
#             dfs(i)
#             cnt += 1
#
#     print(f'#{t}', cnt)
