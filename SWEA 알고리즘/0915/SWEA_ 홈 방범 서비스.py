
for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    home = []
    total = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                home.append([i, j])
                total += 1

    total = 0
    home_c = 0
    for c in range(N):
        for r in range(N):
            ans = [0] * (N * 2)
            table = []
            for y, x in home:
                n = abs(c - y) + abs(r - x)
                table.append(n)
                ans[n + 1] += 1

            count = 0
            for K in range(N * 2):
                if 0 <= M * ans[K] - K * K + (K - 1) * (K - 1):
                    count


    print(total)
