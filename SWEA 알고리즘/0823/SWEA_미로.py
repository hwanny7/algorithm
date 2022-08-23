def go(x, y):
    dr = [0, 0, -1, 1]     #상, 하, 좌, 우
    dc = [-1, 1, 0, 0]
    visited[y][x] = 1
    if arr[y][x] == '3':
        return 3

    for i in range(4):
        if 0 <= x + dr[i] < N and 0 <= y + dc[i] < N and (arr[y + dc[i]][x + dr[i]] == '0' or arr[y + dc[i]][x + dr[i]] == '3') and visited[y + dc[i]][x + dr[i]] == 0:
            result = go(x + dr[i], y + dc[i])
            if result == 3:
                return 3        # 리턴이 3이 오면 더이상 실행하지 말고 return 3을 계속 반환해. 리턴이 3이 오면 밑에 else는 더이상 실행되지 않음.
    else:
        return


for t in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    x = y = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                x, y = j, i
    if go(x, y) == 3:
        print(f'#{t}', 1)
    else:
        print(f'#{t}', 0)


