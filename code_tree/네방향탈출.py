

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

queue = [(0, 0)]

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

visited = [[0 for _ in range(M)] for _ in range(N)]

ans = 0

while queue:
    c, r = queue.pop(0)
    if (c, r) == (N - 1, M - 1):
       ans = 1
       break

    for i in range(4):
        nc, nr = c + dc[i], r + dr[i]
        if 0 <= nc < N and 0 <= nr < M and arr[nc][nr] != 0 and not visited[nc][nr]:
            queue.append((nc, nr))
            visited[nc][nr] = 1

print(ans)