for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    home = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                home.append([i, j])

    cnt = 0
    for c in range(N):
        for r in range(N):
            ans = [0] * (N * 2)

            for y, x in home:
                n = abs(c - y) + abs(r - x) + 1
                ans[n] += 1

            total = 0
            for K in range(1, N * 2):
                total += ans[K]
                L = M * total - (K * K + (K - 1) * (K - 1))
                if 0 <= L and cnt < total:
                    cnt = total

    print(f'#{t}', cnt)