def bfs(C, R):
    lst = [[C, R]]
    dr = [0, 1]     # 하, 우
    dc = [1, 0]
    queue = [[C, R]]
    while queue:
        c, r = queue.pop()
        for i in range(2):
            nc = c + dc[i]
            nr = r + dr[i]
            if 0 <= nc < N and 0 <= nr < N and arr[nc][nr] == '#':
                arr[nc][nr] = '.'
                queue.append([nc, nr])
                lst.append([nc, nr])
    lst.sort()

    if len(lst) == (lst[-1][0] - lst[0][0] + 1) ** 2:
        return 1
    else:
        return 0


for t in range(1, int(input()) + 1):
    ans = []
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == '#':
                ans.append(bfs(i, j))

    if len(ans) == 1 and ans[0] == 1:
        print(f'#{t}', 'yes')
    else:
        print(f'#{t}', 'no')



