
for t in range(1, int(input()) + 1):
    N = int(input())

    arr = [list(input()) for _ in range(N)]


    # 대각선

    ans = 0

    for i in range(N):      # 행, 열
        r = 0
        c = 0
        for j in range(N):
            if arr[i][j] == 'o':
                r += 1
                if 5 <= r:
                    ans += 1
                    break
            else:
                r = 0

            if arr[j][i] == 'o':
                c += 1
                if 5 <= c:
                    ans += 1
                    break
            else:
                c = 0

    dr = [-1, 1]     # 좌 대각, 우 대각
    dc = [1, 1]
    for i in range(N):
        for j in range(N):
            cross1 = 0
            cross2 = 0
            if arr[i][j] == 'o':
                cross1 += 1
                cross2 += 1
                r = j
                c = i
                while True:
                    if 0 <= r + dr[0] < N and 0 <= c + dc[0] < N and arr[c + dc[0]][r + dr[0]] == 'o':
                        cross1 += 1
                        r += dr[0]
                        c += dc[0]
                    else:
                        break

                while True:
                    if 0 <= r + dr[1] < N and 0 <= c + dc[1] < N and arr[c + dc[1]][r + dr[1]] == 'o':
                        cross2 += 1
                        r += dr[1]
                        c += dc[1]
                    else:
                        break
                if 5 <= cross1 or 5 <= cross2:
                    ans += 1
                    break
    if ans:
        print(f'#{t} YES')
    else:
        print(f'#{t} NO')

