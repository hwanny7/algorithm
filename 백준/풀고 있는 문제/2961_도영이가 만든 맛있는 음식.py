# N = int(input())
# food = []
# for i in range(N):
#     taste = list(map(int, input().split()))
#     food.append(taste)
#
# ans = 1000000000
#
# for i in range(1, 1 << N):
#     taste_1 = 1
#     taste_2 = 0
#     for j in range(N):
#         if i & (1 << j):
#             taste_1 *= food[j][0]
#             taste_2 += food[j][1]
#     if ans > abs(taste_1 - taste_2):
#         ans = abs(taste_1 - taste_2)
#
# print(ans)
#
