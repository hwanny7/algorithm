def dessert(c, r, total, i, j, k = 0):
    global ans

    if [c, r] == [i, j]:
        ans = max(len(total) - 1, ans)
        return
    C = c + dc[k]
    R = r + dr[k]

    if 0 <= C < N and 0 <= R < N:
        if C == i or arr[C][R] not in total:
            dessert(C, R, total + [arr[C][R]], i, j, k)
    if 3 < k + 1:
        return

    C1 = c + dc[k + 1]
    R1 = r + dr[k + 1]

    if 0 <= C1 < N and 0 <= R1 < N:
        if C == i or arr[C1][R1] not in total:
            dessert(C1, R1, total + [arr[C1][R1]], i, j, k + 1)

for t in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr = [1, -1, -1, 1]
    dc = [1, 1, -1, -1]

    ans = -1
    for i in range(N - 2):
        for j in range(1, N - 1):
            if arr[i][j] != arr[i + 1][j + 1]:
                dessert(i + 1, j + 1, [arr[i][j], arr[i + 1][j + 1]], i, j)

    print(f'#{t}', ans)