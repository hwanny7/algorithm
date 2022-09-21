# def f(i, k):
#     if i == k:      # 인덱스 i == 원소의 개수
#         print(p)
#     else:
#         for j in range(i, k):
#             p[i], p[j] = p[j], p[i]
#             f(i+1, k)
#             p[i], p[j] = p[j], p[i]
#
# p = [1, 2, 3]
# f(0, 3)

#============================================

# def f(i, k):
#     if i == k:
#         print(p)
#     else:
#         for j in range(k):
#             if used[j] == 0:        # a[j]가 아직 사용되지 않았으면
#                 used[j] = 1         # a[j]가 사용됨으로 표시
#                 p[i] = a[j]         # p[i]는 a[j]로 결정
#                 f(i+1, k)
#                 used[j] = 0
#
#
# N = 3
# a = [i for i in range(1, N + 1)]
# used = [0] * N
# p = [0] * N
# f(0, N)

#===================================================

# def f(i, k, r):
#     if i == r:
#         print(p)
#     else:
#         for j in range(k):
#             if used[j] == 0:        # a[j]가 아직 사용되지 않았으면
#                 used[j] = 1         # a[j]가 사용됨으로 표시
#                 p[i] = a[j]         # p[i]는 a[j]로 결정
#                 f(i+1, k, r)
#                 used[j] = 0
#
#
# N = 10          # 10개(N) 중에 3개(R)만 고를 때
# R = 3
# a = [i for i in range(1, N + 1)]
# used = [0] * N
# p = [0] * R
# f(0, N, R)
