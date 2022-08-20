#
# n = int(input())
#
# arr = [[0] * 1001 for _ in range(1001)]
#
# num = 1
#
# counting = [0] * (n + 1)
#
# for i in range(n):
#     x1, y1, x2, y2 = map(int, input().split())
#     for c in range(y1, y1+y2):
#         for r in range(x1, x1+x2):
#             if arr[c][r] != 0:
#                 counting[arr[c][r]] -= 1
#                 arr[c][r] = num
#                 counting[num] += 1
#             else:
#                 arr[c][r] = num
#                 counting[num] += 1
#
#     num += 1
#
# for i in range(1, len(counting)):
#     print(counting[i])

import sys
input = sys.stdin.readline

n = int(input())


x_max = 0
y_max = 0
lst = []
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    lst.append((x1, y1, x2, y2))
    if x_max < x1 + x2:
        x_max = x1 + x2
    if y_max < y1 + y2:
        y_max = y1 + y2

arr = [[0] * x_max for _ in range(y_max)]

counting = [0] * (n + 1)
num = 1
for x1, y1, x2, y2 in lst:
    for c in range(y1, y1+y2):
        for r in range(x1, x1+x2):
            if arr[c][r] != 0:
                counting[arr[c][r]] -= 1
                arr[c][r] = num
                counting[num] += 1
            else:
                arr[c][r] = num
                counting[num] += 1
    num += 1

for i in range(1, len(counting)):
    print(counting[i])
