import sys
input = sys.stdin.readline

def bfs(i, j):
    global tSheep
    global tWolf
    visit[i][j] = 1
    queue = [(i, j)]

    dc = [-1, 1, 0, 0]
    dr = [0, 0, -1, 1]
    sheep = 0
    wolf = 0

    while queue:
        c, r = queue.pop(0)
        if arr[c][r] == 'v':
            wolf += 1
        elif arr[c][r] == 'o':
            sheep += 1
        for k in range(4):
            nc = c + dc[k]
            nr = r + dr[k]
            if 0 <= nc < N and 0 <= nr < M and arr[nc][nr] != '#' and not visit[nc][nr]:
                queue.append((nc, nr))
                visit[nc][nr] = 1


    if sheep > wolf:
        tSheep += sheep
    else:
        tWolf += wolf



N, M = map(int, input().split())

arr = [list(input()) for _ in range(N)]

visit = [[0] * M for _ in range(N)]

tSheep = 0
tWolf = 0

for i in range(N):
    for j in range(M):
        if not visit[i][j] and arr[i][j] != '#':
            bfs(i, j)


print(tSheep, tWolf)

