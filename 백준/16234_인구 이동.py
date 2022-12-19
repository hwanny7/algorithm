import sys
from collections import deque
input = sys.stdin.readline

def bfs(c, r):
    visit[c][r] = False
    Q = deque()
    Q.append([c, r])
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    change_lst = deque()
    change_lst.append([c, r])
    total = land[c][r]
    while Q:
        c, r = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nc < N and 0 <= nr < N and visit[nc][nr]:
                if L <= abs(land[nc][nr] - land[c][r]) <= R:
                    visit[nc][nr] = False
                    Q.append([nc, nr])
                    change_lst.append([nc, nr])
                    total += land[nc][nr]

    l = len(change_lst)
    if 1 < l:
        for c, r in change_lst:
            land[c][r] = total // l
        return 1
    else:
        return 0



N, L, R = map(int, input().split())
land = []
for i in range(N):
    arr = list(map(int, input().split()))
    land.append(arr)

ans = 0
while True:
    visit = [[True] * N for _ in range(N)]
    check = 0
    for i in range(N):
        for j in range(N):
            if visit[i][j]:
                check += bfs(i, j)
    if check:
        ans += 1
    else:
        break
print(ans)
