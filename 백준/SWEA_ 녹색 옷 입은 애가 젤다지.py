from heapq import heappop, heappush

num = 0
while True:
    num += 1
    N = int(input())
    if not N:
        break
    arr = [list(map(int, input().split())) for _ in range(N)]
    queue = []
    visit = [[0] * N for _ in range(N)]
    heappush(queue, (arr[0][0], 0, 0))
    while queue:
        value, c, r = heappop(queue)
        if visit[c][r]: continue
        if [c, r] == [N - 1, N - 1]:
            print(f'Problem {num}: {value}')
            break
        visit[c][r] = 1
        dr = [0, 0, -1, 1]
        dc = [-1, 1, 0, 0]
        for i in range(4):
            C = c + dc[i]
            R = r + dr[i]
            if 0 <= C < N and 0 <= R < N:
                heappush(queue, (value + arr[C][R], C, R))






