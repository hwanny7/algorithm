from collections import deque


def bfs():
    visitied[0][0][0] = 1
    queue = deque()
    queue.append([0, 0, 0])
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    while queue:
        c, r, cnt = queue.popleft()
        for i in range(4):
            C = dc[i] + c
            R = dr[i] + r
            if 0 <= C < N and 0 <= R < N:
                temp = cnt
                if arr[C][R] == 0:      #벽일 때 cnt + 1
                    temp = cnt + 1
                if visitied[C][R][0]:   #방문 한 적 있을 때
                    if visitied[C][R][1] > temp:
                        visitied[C][R][1] = temp
                        queue.append([C, R, temp])
                else:                   #방문 한 적 없을 때
                    visitied[C][R][0] = 1
                    visitied[C][R][1] = temp
                    queue.append([C, R, temp])


N = int(input())

arr = [list(map(int, input())) for _ in range(N)]
visitied = [[[0, 0] for _ in range(N)] for _ in range(N)]

bfs()

print(visitied[N - 1][N - 1][1])