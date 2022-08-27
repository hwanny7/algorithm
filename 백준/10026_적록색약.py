
def bps(C, R, V):
    dr = [0, 0, -1, 1]     #상, 하, 좌, 우
    dc = [-1, 1, 0, 0]
    visited[C][R] = 1
    queue = [[C, R]]
    while queue:
        c, r = queue.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nc < N and 0 <= nr < N and visited[nc][nr] == 0:
                if V == 1 and arr[nc][nr] == 'R':
                    queue.append([nc, nr])
                    visited[nc][nr] = 1
                elif V == 2 and arr[nc][nr] == 'B':
                    queue.append([nc, nr])
                    visited[nc][nr] = 1
                elif V == 3 and arr[nc][nr] == 'G':
                    queue.append([nc, nr])
                    visited[nc][nr] = 1
    return 1

def GRF(C ,R):
    dr = [0, 0, -1, 1]  # 상, 하, 좌, 우
    dc = [-1, 1, 0, 0]
    visited[C][R] = 2
    temp = [[C, R]]
    while temp:
        c, r = temp.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nc < N and 0 <= nr < N and visited[nc][nr] == 1:
                if arr[nc][nr] == 'R':
                    temp.append([nc, nr])
                    visited[nc][nr] = 2
                elif arr[nc][nr] == 'G':
                    temp.append([nc, nr])
                    visited[nc][nr] = 2

    return 1

N = int(input())
visited = [[0] * N for _ in range(N)]
arr = [list(input()) for _ in range(N)]
GR = []
total = 0
total2 = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            if arr[i][j] == 'R':
                GR.append([i, j])
                total += bps(i, j, 1)
            elif arr[i][j] == 'B':
                n = bps(i, j, 2)
                total += n
                total2 += n
            else:
                GR.append([i, j])
                total += bps(i, j, 3)

for c, r in GR:
    if visited[c][r] == 1:
        total2 += GRF(c, r)

print(total, total2)


