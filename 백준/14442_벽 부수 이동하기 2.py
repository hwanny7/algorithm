import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    global CNT
    dr = [0, 0, -1, 1]     #하, 좌, 우
    dc = [-1, 1, 0, 0]
    visited[x][y][CNT] = 1
    queue = deque()
    queue.append([x, y, CNT])
    while queue:        # visited 먼저 방문하는 놈 때문에 우선순위 문제가 생겨남
        c, r, count = queue.popleft()
        for i in range(4):
            C = c + dc[i]
            R = r + dr[i]
            if 0 <= C < N and 0 <= R < M:
                if arr[C][R] == 0 and visited[C][R][count] == 0:
                    visited[C][R][count] = visited[c][r][count] + 1
                    queue.append([C, R, count])
                elif arr[C][R] == 1 and count >= 1 and visited[C][R][count - 1] == 0:
                    visited[C][R][count - 1] = visited[c][r][count] + 1
                    queue.append([C, R, count - 1])

N, M, CNT = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0] * (CNT + 1) for _ in range(M)] for _ in range(N)]
bfs(0, 0)


cnt = 1000000000000000000000
for i in visited[N-1][M -1]:
    if i != 0 and cnt > i:
        cnt = i
if cnt == 1000000000000000000000:
    print(-1)
else:
    print(cnt)