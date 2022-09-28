


for t in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int , input().split())) for _ in range(N)]
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    INF = 999999999
    visit = [[INF] * N for _ in range(N)]
    visit[0][0] = 0
    queue = [[0, 0]]

    while queue:
        c, r = queue.pop(0)
        for i in range(4):
            C = c + dc[i]
            R = r + dr[i]
            if 0 <= C < N and 0 <= R < N:
                temp = 1 + visit[c][r]
                if arr[C][R] > arr[c][r]:
                    temp += arr[C][R] - arr[c][r]
                if temp < visit[C][R]:
                    visit[C][R] = temp
                    queue.append((C, R))

    print(f'#{t}', visit[N - 1][N - 1])





