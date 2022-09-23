def dessert(c, r, total, i, j, start = 0):

for t in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr = [1, -1, -1, 1]
    dc = [1, 1, -1, -1]

    for i in range(N - 2):
        for j in range(1, N -1):
            dessert(i, j, [arr[i][j]], i, j)

    print(ans)