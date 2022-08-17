di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N = 3
M = 4
arr = [[1,2,3,4], [4,5,6,7]]
for i in range(N):
    for j in range(M):
        for k in range(4): # 방향이 4개
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<M:  #n과 m을 나갈 경우 배열을 이탈한다.
                print([i, j], ni, nj)

# for i in range(N):     #다른 방법
#     for j in range(M):
#         for di, dj in [[0,1], [1, 0], [0,-1], [-1, 0]]:
#             ni, nj = i + di, j+ dj
#             if 0 <= ni <N and 0<=nj<M:
#                 print(ni, nj)
#
#
# for i in range(N):
#     for j in range(M):
#         for d in range(1, 3):       # 바로 옆이 아닌 거리가 더 큰 인접한 배열을 구하는 경우
#             for k in range(4): # 방향이 4개
#                 ni = i + di[k]
#                 nj = j + dj[k]
#                 if 0<=ni<N and 0<=nj<M:
#                     print(ni, nj)