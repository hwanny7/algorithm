

for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    total = 0
    for i in range(M):
        y, x, l = map(int, input().split())
        for j in range(l):
            for k in range(l):
                if 0 <= y + j < N and 0 <= x + k < N:
                    total += arr[y + j][x + k]
                    arr[y + j][x + k] = 0

    print(f'#{t}', total)