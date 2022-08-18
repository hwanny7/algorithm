def dfs(v, end):
    visited = [0] * 100
    stack = [0] * 100
    top = -1
    visited[v] = 1

    while True:
        for w in adjlist[v]:
            if visited[w] == 0:
                visited[w] = 1
                if w == 99:
                    return 1
                top += 1
                stack[top] = v
                v = w
                break
        else:
            if top != -1:
                v = stack[top]
                top -= 1
            else:
                return 0




for t in range(10):
    T, load = map(int, input().split())
    adjlist = [[] for _ in range(100)]
    nums = list(map(int, input().split()))
    for i in range(1, len(nums), 2):
        adjlist[nums[i-1]].append(nums[i])

    print(f'#{T}', dfs(0, 99))