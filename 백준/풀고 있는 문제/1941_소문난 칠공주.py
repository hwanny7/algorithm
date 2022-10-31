import sys
sys.setrecursionlimit(150000)

def find(c, r, s = 1, y = 0, lst = []):
    global cnt
    cnt += 1
    global ans
    if y >= 4:
        return

    if s + y == 7:
        ans += 1
        return

    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    for i in range(4):
        nc = c + dc[i]
        nr = r + dr[i]
        if 0 <= nc < 5 and 0 <= nr < 5:
            if visit[nc][nr]:
                find(nc, nr, s, y, lst)
            else:
                if arr[nc][nr] == 'S':
                    visit[nc][nr] = True
                    find(nc, nr, s + 1, y, lst + [nc, nr])
                    visit[nc][nr] = False
                else:
                    visit[nc][nr] = True
                    find(nc, nr, s, y + 1, lst + [nc, nr])
                    visit[nc][nr] = False

arr = [list(input())for _ in range(5)]
ans = 0
cnt = 0
visit = [[False] * 5 for _ in range(5)]
for i in range(5):
    for j in range(5):
        if arr[i][j] == 'S':
            visit[i][j] = True
            find(i, j)
            visit[i][j] = False

print(cnt)
print(ans)