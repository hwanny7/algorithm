import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    dr = [0, 0, -1, 1]     #하, 좌, 우
    dc = [-1, 1, 0, 0]
    visited[x][y][1] = 1
    queue = deque()
    queue.append([x, y, 1])
    while queue:        # visited 먼저 방문하는 놈 때문에 우선순위 문제가 생겨남
        c, r, count = queue.popleft()
        for i in range(4):
            C = c + dc[i]
            R = r + dr[i]
            if 0 <= C < N and 0 <= R < M:
                if arr[C][R] == 0 and visited[C][R][count] == 0:
                    visited[C][R][count] = visited[c][r][count] + 1
                    queue.append([C, R, count])
                elif arr[C][R] == 1 and count == 1 and visited[C][R][0] == 0:
                    visited[C][R][0] = visited[c][r][count] + 1
                    queue.append([C, R, 0])

N, M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
bfs(0, 0)

for i in visited:
    print(i)

cnt = 0
for i in visited[N-1][M -1]:
    if i == 0:
        cnt += 1
if cnt == 2:
    print(-1)
elif cnt == 1:
    print(max(visited[N-1][M -1]))
else:
    print(min(visited[N-1][M -1]))

