dc = [-1, 1, 0, 0]
dr = [0, 0, -1, 1]



def dfs(c, r, cnt = 0):
    global ans
    if (c, r) == (0, R - 1) and cnt == K - 1:
        ans += 1
        return


    for i in range(4):
        nc = c + dc[i]
        nr = r + dr[i]
        if 0 <= nc < C and 0 <= nr < R and not visit[nc][nr] and arr[nc][nr] != 'T':
            visit[nc][nr] = True
            dfs(nc, nr, cnt + 1)
            visit[nc][nr] = False









C, R, K = map(int, input().split())

arr = [list(input()) for _ in range(C)]
visit = [[False for _ in range(R)] for _ in range(C)]
visit[C - 1][0] = True
ans = 0
dfs(C - 1, 0)
print(ans)