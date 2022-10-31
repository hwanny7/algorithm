# N, K = map(int, input().split())
#
# p = 0
# ans = [0] * (K + 1)
# for i in range(N):
#     w, v = map(int, input().split())
#     temp = [0] * (K + 1)
#     for i in range(K + 1):
#         if i < w:
#             temp[i] = ans[i]
#             p = max(p, temp[i])
#         else:
#             temp[i] = max(ans[i], v, ans[i - w] + v)
#             p = max(p, temp[i])
#     ans = temp[:]
# print(p)

N, K = map(int, input().split())

p = 0
ans = [0] * (K + 1)
for i in range(N):
    w, v = map(int, input().split())
    temp = [0] * (K + 1)
    for i in range(w, K + 1):
        temp[i] = max(ans[i], ans[i - w] + v)
    ans = temp[:]
    p = max(p, temp[i])

print(p)