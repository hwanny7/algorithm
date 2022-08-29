import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    global changed
    global visit
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    while queue:
        c, r = queue.popleft()
        for i in range(4):
            nc = c + dc[i]
            nr = r + dr[i]
            if 0 <= nc < Y and 0 <= nr < X and arr[nc][nr] == 0:
                changed += 1
                queue.append([nc, nr])
                arr[nc][nr] = arr[c][r] + 1
                if visit < arr[nc][nr]:
                    visit = arr[nc][nr]


X, Y = map(int, input().split())
visit = 0
total = 0       #익지 않은 토마토 갯수
changed = 0
arr = [list(map(int, input().split())) for _ in range(Y)]
queue = deque()
for i in range(Y):
    for j in range(X):
        if arr[i][j] == 0:
            total += 1
        elif arr[i][j] == 1:
            queue.append([i, j])

bfs()
if total == 0:
    print(0)
elif total == changed:
    print(visit - 1)
else:
    print(-1)