for t in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    idx = [[] for _ in range(N ** 2 + 2)]

    for i in range(N):
        for j in range(N):
            idx[arr[i][j]] = [i, j]

    idx[-1] = [10000, 10000]
    Grand = number = 0
    num = 1
    total = 1
    for i in range(1, N ** 2 + 1):
        C, R = idx[i]
        c, r = idx[i + 1]
        if abs(C - c) + abs(R - r) == 1:
            total += 1
            continue
        if Grand < total:
            Grand = total
            number = num
        num = i + 1
        total = 1

    print(f'#{t}', number, Grand)