def dfs(S):
    visited = [0] * N
    visited[S] = 1
    queue = [[S, str(S + 1)]]
    while queue:
        S, ans = queue.pop(0)
        for i in range(N):
            if visited[i]:
                continue
            n = int(arr[i], 2)^int(arr[S], 2)
            if n & (n - 1) == 0:
                temp = ans + str(i + 1)
                if i + 1 == end:
                    return temp
                queue.append([i, temp])
                visited[i] = 1



N, K = map(int, input().split())
arr = [input() for _ in range(N)]
start, end = map(int, input().split())


if start == end:        #시작이랑 끝이 같을 때
    print(start, end)
else:
    ans = dfs(start - 1)
    if ans:
        for i in ans:
            print(i, end=' ')
    else:
        print(-1)

# print(int('000', 2)^int('000', 2))
# print(16 & 15)