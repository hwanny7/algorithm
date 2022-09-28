def dfs(x, o):
    visit[x] = o
    for i in V[x]:
        if not visit[i]:
            dfs(i, o)

for t in range(1, int(input()) + 1):
    people, paper = map(int, input().split())
    arr = list(map(int, input().split()))
    V = [[] for i in range(people + 1)]
    for i in range(0, paper * 2, 2):
        V[arr[i]].append(arr[i + 1])
        V[arr[i + 1]].append(arr[i])
    visit = [0] * (people + 1)
    cnt = -1
    for i in range(1, people + 1):
        if not visit[i]:
            dfs(i, i)

    print(f'#{t}', len(set(visit)) + cnt)