def bfs():
    visit = [[99999] * N for _ in range(N)]
    visit[0][0] = 0
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    queue = [[0, 0]]

    while queue:
        for i in range(len(queue)):
            c, r = queue.pop(0)
            for i in range(4):
                C = c + dc[i]
                R = r + dr[i]
                if 0 <= C < N and 0 <= R < N:
                    temp = visit[c][r] + arr[C][R]
                    if temp < visit[C][R]:
                        visit[C][R] = temp
                        queue.append([C, R])
        print(queue)

    print(f'#{t}', visit[N - 1][N - 1])


for t in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    bfs()