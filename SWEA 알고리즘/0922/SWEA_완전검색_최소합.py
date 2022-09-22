

def bfs(c, r):
    visited[c][r] = arr[c][r]
    queue = [[c, r]]
    dr = [0, 1]
    dc = [1, 0]
    while queue:
        c, r = queue.pop(0)
        for i in range(2):
            C = c + dc[i]
            R = r + dr[i]
            if 0 <= C < N and 0 <= R < N:
                V = visited[c][r] + arr[C][R]
                if visited[C][R] and visited[C][R] > V:
                    visited[C][R] = V
                    queue.append([C, R])
                elif not visited[C][R]:
                    visited[C][R] = V
                    queue.append([C, R])


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    bfs(0, 0)
    print(f'#{tc}', visited[N-1][N-1])




# def dfs(c, r, total):
#     global min
#     dr = [0, 1]
#     dc = [1, 0]
#     if c == N - 1 and r == N - 1:
#         if min > total:
#             min = total
#         return
#     if min < total:
#         return
#     for i in range(2):
#         C = c + dc[i]
#         R = r + dr[i]
#         if 0 <= C < N and 0 <= R < N:
#             dfs(C, R, total + arr[C][R])
#
# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     min = N ** 2 * 10
#     dfs(0, 0, arr[0][0])
#     print(f'#{tc}', min)