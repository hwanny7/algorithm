def dfs(num):
    print(num)
    if visit[num] == 1:
        return
    visit[num] = 1

    for i in range(N):
        if arr[num - 1][i]:
            arr[i][num - 1] = 1
            dfs(i + 1)




N = int(input())
visit = [0] * (N + 1)
arr = [list(map(int, input().split())) for _ in range(N)]

dfs(1)

for i in arr:
    print(i)
