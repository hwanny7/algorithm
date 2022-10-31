# N = int(input())
# arr = list(map(int, input().split()))
#
# value = [0xffffffff] * N
# value[0] = arr[0]
# idx = 0
# for i in range(1, N):
#     for j in range(i - 1, -1, -1):
#         if value[j] < arr[i]:
#             value[j + 1] = arr[i]
#             break
#     else:
#         if value[0] > arr[i]:
#             value[0] = arr[i]
# print(value)

N = int(input())
arr = list(map(int, input().split()))

value = [0xffffffff] * N
value[0] = arr[0]
idx = 0
for i in range(1, N):
    if value[idx] < arr[i]:
        value[j + 1] = arr[i]
        idx = max(idx, j + 1)
        break
    else:
        if value[0] > arr[i]:
            value[0] = arr[i]

print(idx + 1)
print(*value[:idx + 1])