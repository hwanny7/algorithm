import sys
from collections import deque
input = sys.stdin.readline

def find(c, r):
    global flag
    visit[c][r] = False
    arr[c][r] = flag
    Q = deque()
    Q.append([c, r])
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    while Q:
        c, r = Q.popleft()
        cnt = 0
        for i in range(4):
            nc = c + dc[i]
            nr = r + dr[i]
            if 0 <= nc < N and 0 <= nr < N:
                if arr[nc][nr] and visit[nc][nr]:
                    arr[nc][nr] = flag
                    visit[nc][nr] = False
                    Q.append([nc, nr])
                elif arr[nc][nr] == 0:
                    cnt += 1
        if cnt:
            key.append([c, r])

    flag += 1

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[True]* N for _ in range(N)]
flag = 1
key = deque()
for i in range(N):
    for j in range(N):
        if arr[i][j] and visit[i][j]:
            find(i, j)

visit = [[0] * N  for _ in range(N)]
ans = 0xffffffffffffff

while key:
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    c, r = key.popleft()
    for i in range(4):
        nc = c + dc[i]
        nr = r + dr[i]
        if 0 <= nc < N and 0 <= nr < N:
            if arr[nc][nr] == 0:
                arr[nc][nr] = arr[c][r]
                visit[nc][nr] = visit[c][r] + 1
                key.append([nc, nr])
            elif arr[nc][nr] != arr[c][r]:
                if ans > visit[nc][nr] + visit[c][r]:
                    ans = visit[nc][nr] + visit[c][r]

print(ans)

for i in arr:
    print(*i)
print()
for i in visit:
    print(*i)