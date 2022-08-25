N = int(input())

arr = []

for i in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))
arr.sort()

max = 0
for i in range(1, len(arr)):
    if arr[i][1] > arr[max][1]:
        max = i

total = 0
max = arr[i][1]

for i in range(0, max):
    h = arr[i][1]
    w = arr[i][0]
    total += arr[i]
    if max >= arr[i][1]:
        total += (arr[i + 1][0] - arr[i][0] + 1) * arr[i][1]

print(total)


# N = int(input())
#
# lst = []
#
# for i in range(N):
#     x, y = map(int, input().split())
#     lst.append((x, y))
# lst.sort()
#
#
# for i in range(N):
#     w = lst[i][0]
#     h = lst[i][1]
#
#     total += h
#     high = h
#     width = w
#
#     if h >= high:
#         total += w -
#         h = h1
#         w = w1
#     else:           # 작은 경우
#         for j in range(i + 1, N):
#             if lst[j][1] > h1:
#                 break
#         else:
#             total += (w1 - w) * h1 + h - h1
#             h = h1
#             w = w1
#
# print(total)



