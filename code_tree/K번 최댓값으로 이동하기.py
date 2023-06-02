
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def bfs(C, R, cnt):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[C][R] = 1
    queue = [(C, R)]
    base_num = arr[C][R]
    max_cr = (0, 0, 0)
    while queue:
        c, r = queue.pop(0)

        for i in range(4):
            nc, nr = c + dc[i], r + dr[i]
            if 0 <= nc < N and 0 <= nr < N and not visited[nc][nr] and arr[nc][nr] < base_num:
                queue.append((nc, nr))
                visited[nc][nr] = 1
                num, cur_c, cur_r = max_cr

                if (num, -cur_c, -cur_r) < (arr[nc][nr], -nc, -nr):
                    max_cr = (arr[nc][nr], nc, nr)


    num, c, r = max_cr

    if num:
        if K == cnt:
            return (c + 1, r + 1)
        else:
            return bfs(c, r, cnt + 1)
    else:
        return (C + 1, R + 1)




N, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
C, R = map(int, input().split())
print(*bfs(C - 1, R - 1, 1))
