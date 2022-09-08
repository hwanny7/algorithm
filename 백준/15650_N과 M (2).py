# def bfs(K, J):
#     if M == K - 1:
#         print(*arr[1:])
#         return
#     else:
#         for i in range(1 + J, N + 1):
#             if i > arr[K - 1]:
#                 arr[K] = i
#                 bfs(K + 1, J + 1)
#
# N, M = map(int, input().split())
# arr = [0] * (M + 1)
# bfs(1, 0)

#수정본
def bfs(K, J):
    if K == M:
        print(*arr)
        return
    else:
        for i in range(1, N + 1):
            if i > J:
                arr[K] = i
                bfs(K + 1, i)


N, M = map(int, input().split())
arr = [0] * M
bfs(0, 0)

