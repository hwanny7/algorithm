import sys; sys.stdin = open('파리퇴치3.txt')


for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # for i in arr:
    #     print(*i)

    dr = [0, 0, -1, 1, +1, +1, -1, -1]  #상, 하, 좌, 우, 대각선
    dc = [-1, 1, 0, 0, -1, +1, +1, -1]

    g_total = []

    for i in range(N):
        for j in range(N):
            total = arr[i][j]
            total2 = arr[i][j]
            C = M
            while 1 < C:            # 좌표에 곱할 변수 C 생성
                C -= 1
                for k in range(4):
                    if 0 <= i + dc[k] * C < N and 0 <= j + dr[k] * C < N:             # + 모양
                        total += arr[i+dc[k] * C][j+dr[k] * C]
                    if 0 <= i + dc[k+4] * C < N and 0 <= j + dr[k+4] * C < N:        # 대각선 모양
                        total2 += arr[i+dc[k+4] * C][j+dr[k+4] * C]
            g_total.append(total)
            g_total.append(total2)

    max = 0
    for m in g_total:
        if max < m:
            max = m
    print(f'#{t}', max)


