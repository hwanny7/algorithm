for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())    # M은 폭탄 갯수

    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [0, 0, -1, 1]     # 상, 하, 좌, 우
    dc = [-1, 1, 0, 0]

    total = 0
    for i in range(M):
        c, r, p= map(int, input().split())  # 행, 열, 범위
        total += arr[c][r]
        arr[c][r] = 0
        for i in range(1, p + 1):
            for j in range(4):
                if 0 <= c + dc[j] * i < N and 0 <= r + dr[j] * i < N:
                    total += arr[c + dc[j] * i][r + dr[j] * i]
                    arr[c + dc[j] * i][r + dr[j] * i] = 0

    print(f'#{t}', total)
