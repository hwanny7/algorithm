

for t in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    S = N // 2

    g_total = 0
    for i in range(N):
        total = arr[i][S]
        for j in range(1, i + 1):
                total += arr[i][S - j] + arr[i][S + j]

        g_total += total

