

N = int(input())
r1, c1, r2, c2 = map(int, input().split())

queue = [(r1, c1)]
visit = [[0] * N for _ in range(N)]
ans = 0

dr = [-2, -2, 0, 0, 2, 2]
dc = [-1, 1, -2, 2, -1, 1]


while queue:

    for i in range(len(queue)):
        r1, c1 = queue.pop(0)
        if (r1, c1) == (r2, c2):
            print(ans)
            exit(0)
        for i in range(6):
            nr = r1 + dr[i]
            nc = c1 + dc[i]
            if 0 <= nr < N and 0 <= nc < N and not visit[nc][nr]:
                queue.append((nr, nc))
                visit[nc][nr] = 1
    ans += 1

print(-1)

