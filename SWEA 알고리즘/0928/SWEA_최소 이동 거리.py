#=================================다익스트라
# def dik(S, E):
#     INF = 1000000 * 10
#     U = [0] * (V + 1)
#     U[S] = 1
#     D = [INF] * (V + 1)
#     D[0] = 0
#     for e, w in adjL[S]:
#         D[e] = w
#
#     for _ in range(V - 1):      #첫번째와 마지막은 정해져 있음
#         minV = INF
#         idx = 0
#         for i in range(1, V):   # 0번과 V는 정해져 있기 때문에 이 범위로
#             if U[i] == 0 and minV > D[i]:
#                 minV = D[i]
#                 idx = i
#
#         U[idx] = 1
#
#         for e, w in adjL[idx]:
#             D[e] = min(D[e] , minV + w)
#
#     print(f'#{t}', D[V])
#
#
# for t in range(1, int(input()) + 1):
#     V, E = map(int, input().split())
#     adjL = [[] for _ in range(V)]
#     for i in range(E):
#         s, e, w = map(int, input().split())
#         adjL[s].append((e, w))
#     dik(0, V)












#=========================== BFS로 푸는 방법
# for t in range(1, int(input()) + 1):
#     N, E = map(int, input().split())
#     # 정점 0번부터 N번까지
#     G = [[] for _ in range(N + 1)]
#     for _ in range(E):
#         u, v, weight = map(int, input().split())
#         G[u].append((v, weight))
#
#     D = [0xffffff] * (N + 1)        #거리 저장
#     D[0] = 0                      #출발점 0으로 설정
#     Q = [0]
#
#     while Q:
#         u = Q.pop(0)
#         for v, weight in G[u]:
#             if D[v] > D[u] + weight:
#                 D[v] = D[u] + weight
#                 Q.append(v)
#
#     print(f'#{t} {D[N]}')

#============================================== DFS로 푸는 법
#
# for t in range(1, int(input()) + 1):
#     N, E = map(int, input().split())
#     # 정점 0번부터 N번까지
#     G = [[] for _ in range(N + 1)]
#     for _ in range(E):
#         u, v, weight = map(int, input().split())
#         G[u].append((v, weight))
#
#     D = [0xffffff] * (N + 1)        #거리 저장
#     D[0] = 0                      #출발점 0으로 설정
#     Q = [0]
#
#     def dfs(u):
#         for v, weight in G[u]:
#             if D[v] > D[u] + weight:
#                 D[v] = D[u] + weight
#                 dfs(v)
#     dfs(0)
#     print(f'#{t} {D[N]}')

