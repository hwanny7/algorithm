from heapq import heappop, heappush
for tc in range(1, int(input()) + 1):
    N = int(input())
    MAP = [list(map(int, input())) for _ in range(N)]

    # 다익스트라로 최단 경로 구하기
    visit=[[0] * N for _ in range(N)]
    D = [[0xffffff] * N for _ in range(N)]
    D[0][0] = 0
    Q = []
    heappush(Q, (0, 0, 0))  # (거리, r, c)

    while Q:
        d, r, c = heappop(Q)        #거리가 작은 것부터 꺼낸다.
        if visit[r][c]: continue    #거리가 작은 것부터 들리기 때문에 다음번에 또 같은 곳을 들릴 경우 어처피 최단거리가 아니기 때문에 무시한다.
        visit[r][c] = 1

        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and D[nr][nc] > D[r][c] + MAP[nr][nc]:
                D[nr][nc] = D[r][c] + MAP[nr][nc]
                heappush(Q, (D[nr][nc], nr, nc))

    print(D[N-1][N-1])
