

for t in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [0, 0, -1, 1] #상, 하, 좌, 우
    dc = [-1, 1, 0, 0]

    grand_total = 0
    for c in range(N):
        for r in range(N):
            total = arr[c][r]
            for v in range(1, N):
                for j in range(4):
                    if 0 <= c + dc[j]*v < N and 0 <= r + dr[j]*v < N:
                        total += arr[c + dc[j]*v][r + dr[j]*v]
            if grand_total < total:
                grand_total = total

    print(f'#{t}', grand_total)


