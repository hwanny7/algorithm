
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]



N, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
ans = 0
queue = []
for _ in range(K):
    x, y = map(int, input().split())
    queue.append((x - 1, y - 1))
    visited[x - 1][y - 1] = 1


while queue:
    c, r = queue.pop(0)
    ans += 1
    for i in range(4):
        nc, nr = c + dc[i], r + dr[i]
        if 0 <= nc < N and 0 <= nr < N and not visited[nc][nr] and arr[nc][nr] == 0:
            queue.append((nc, nr))
            visited[nc][nr] = 1

print(ans)

