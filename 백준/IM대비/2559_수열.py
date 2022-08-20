
day, d = map(int, input().split())

nums = list(map(int, input().split()))


# lst = []
# for i in range(day - d + 1):
#     total = 0
#     for j in range(i, i + d):
#         total += nums[j]
#     lst.append(total)
#
# print(max(lst))

V = sum(nums[0:d])
max = V
for i in range(1, day - d + 1):
    V = V - nums[i-1] + nums[d + i - 1]
    if max < V:
        max = V
print(max)