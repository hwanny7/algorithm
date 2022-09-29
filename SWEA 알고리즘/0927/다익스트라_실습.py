'''
5 11
0 1 3
0 2 5
1 2 2
1 3 6
2 1 1
2 3 4
2 4 6
3 4 2
3 5 3
4 0 3
4 5 6
'''
#============= 인접행렬
# def dijkstra(s, V):
#     U = [0]*(V+1)       # 비용이 결정된 정점을 표시
#     U[s] = 1            # 출발점 비용 결정
#     for i in range(V+1):
#         D[i] = adjM[s][i]
#
#     # 남은 정점의 비용 결정
#     for _ in range(V):      # 남은 정점 개수만큼 반복
#         # D[w]가 최소인 w 결정, 비용이 결정되지 않은 정점 w 중에서
#         minV = INF
#         w = 0
#         for i in range(V+1):                #아직 선택되지 않았으면서 비용이 제일 작은 곳을 찾는다.
#             if U[i] == 0 and minV > D[i]:
#                 minV = D[i]
#                 w = i
#         U[w] = 1                # 비용 결정
#         for v in range(V+1):                #비용이 제일 작은 곳에서 다른 곳으로 이동할 때의 비용을 확인
#             if 0 < adjM[w][v] < INF:        #w 에서 v로 가는 간선이 있으면, 자기 자신으로 가는 간선은 제외하기 위해 0으로 설정
#                 D[v] = min(D[v], D[w] + adjM[w][v])
#
# INF = 10000
# V, E = map(int, input().split())
# adjM = [[INF]*(V+1) for _ in range(V+1)]
# for i in range(V+1):
#     adjM[i][i] = 0
# for _ in range(E):
#     u, v, w = map(int, input().split())
#     adjM[u][v] = w
#
# D = [0]*(V+1)
# dijkstra(0, V)
# print(D)

#=============================== 인접리스트
#
# def dijkstra(s, V):
#     U = [0]*(V+1)       # 비용이 결정된 정점을 표시
#     U[s] = 1            # 출발점 비용 결정
#     D[s] = 0
#     for v, w in adjL[s]:
#         D[v] = w
#
#     # 남은 정점의 비용 결정
#     for _ in range(V):      # 남은 정점 개수만큼 반복
#         # D[t]가 최소인 t 결정, 비용이 결정되지 않은 정점t 중에서
#         minV = INF
#         t = 0
#         for i in range(V+1):
#             if U[i] == 0 and minV > D[i]:
#                 minV = D[i]
#                 t = i
#         U[t] = 1                # 비용 결정. 비용이 가장 작은 값일 경우 그 외에 더 빠른 경로가 없다고 판단할 수 있기 때문에 비용 확정.
#         for v, w in adjL[t]:
#                 D[v] = min(D[v], D[t]+w)        #D[v]는 지금까지 발견한 가장 좋은 경로, 아직 갱신이 안 되어 있으면 INF로 되어 있을 것임
#
# INF = 10000                         #가장 큰 값을 설정
# V, E = map(int, input().split())
# adjL = [[] for _ in range(V+1)]
# for _ in range(E):
#     u, v, w = map(int, input().split())
#     adjL[u].append([v, w])
#
# D = [INF]*(V+1)
# dijkstra(0, V)
# print(D)
