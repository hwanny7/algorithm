

for t in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    S = N // 2

    g_total = 0
    for i in range(N):
        total = arr[i][S]
        if i <= S:
            for j in range(1, i + 1):
                total += arr[i][S - j] + arr[i][S + j]
        else:
            for j in range(N - i - 1, 0, -1):
                total += arr[i][S - j] + arr[i][S + j]
        g_total += total

    print(f'#{t}', g_total)

