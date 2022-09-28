# def bfs():
#     visit = [[99999] * N for _ in range(N)]
#     visit[0][0] = 0
#     dr = [0, 0, -1, 1]
#     dc = [-1, 1, 0, 0]
#     queue = [[0, 0]]
#
#     while queue:
#         c, r = queue.pop(0)
#         for i in range(4):
#             C = c + dc[i]
#             R = r + dr[i]
#             if 0 <= C < N and 0 <= R < N:
#                 temp = visit[c][r] + arr[C][R]
#                 if temp < visit[C][R]:
#                     visit[C][R] = temp                            # visit이 최소 값으로 갱신되어 있음. 첫번째 비용: 5, 두번째 비용: 4 로 되어 있을 때
# #                                                                 # 다음 queue에서 꺼내서 visit 을 비교할 경우 visit에 저장된 최근 비용으로 비교하기 때문에 (첫번째 비용 5가 아닌)
# #                                                                 # 중복으로 queue가 생겨나는 것을 막을 수 있다.
#                     queue.append([C, R])
#
#     print(f'#{t}', visit[N - 1][N - 1])
#
#
# for t in range(1, int(input()) + 1):
#     N = int(input())
#     arr = [list(map(int, input())) for _ in range(N)]
#     bfs()

def bfs():
    visit = [[99999] * N for _ in range(N)]
    visit[0][0] = 0
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    queue = [[0, 0]]
    dic = {}
    while queue:
        c, r = queue.pop(0)
        for i in range(4):
            C = c + dc[i]
            R = r + dr[i]
            if 0 <= C < N and 0 <= R < N:
                temp = visit[c][r] + arr[C][R]
                if temp < visit[C][R]:
                    visit[C][R] = temp
                    if not dic.get((C, R)):
                        queue.append([C, R])
                        dic[(C, R)] = 1

    print(f'#{t}', visit[N - 1][N - 1])


for t in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    bfs()