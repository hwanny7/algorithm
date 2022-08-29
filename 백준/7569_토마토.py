import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    global changed
    global visit
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    while queue:
        k, c, r = queue.popleft()
        for i in range(4):
            nc = c + dc[i]
            nr = r + dr[i]
            if 0 <= nc < Y and 0 <= nr < X and arr[k][nc][nr] == 0:
                changed += 1
                queue.append([k, nc, nr])
                arr[k][nc][nr] = arr[k][c][r] + 1
                if visit < arr[k][nc][nr]:
                    visit = arr[k][nc][nr]
        up = k - 1
        under = k + 1
        if 0 <= up < K and arr[up][c][r] == 0:
            changed += 1
            queue.append([up, c, r])
            arr[up][c][r] = arr[k][c][r] + 1
            if visit < arr[up][c][r]:
                visit = arr[up][c][r]
        if 0 <= under < K and arr[under][c][r] == 0:
            changed += 1
            queue.append([under, c, r])
            arr[under][c][r] = arr[k][c][r] + 1
            if visit < arr[under][c][r]:
                visit = arr[under][c][r]


X, Y, K= map(int, input().split())
visit = 0
total = 0       #익지 않은 토마토 갯수
changed = 0
arr = [[list(map(int, input().split())) for _ in range(Y)] for _ in range(K)]
queue = deque()

for k in range(K):
    for i in range(Y):
        for j in range(X):
            if arr[k][i][j] == 0:
                total += 1
            elif arr[k][i][j] == 1:
                queue.append([k, i, j])

bfs()
if total == 0:
    print(0)
elif total == changed:
    print(visit - 1)
else:
    print(-1)