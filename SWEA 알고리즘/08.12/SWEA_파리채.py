
for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    grand_total = 0

    for c in range(N-M+1):
        for r in range(N-M+1):
            total = 0
            for i in range(c, c+M):
                for j in range(r, r+M):
                   total += arr[i][j]
            if grand_total < total:
                grand_total = total

    print(f'#{t}', grand_total)