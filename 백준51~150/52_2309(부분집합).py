
# nums = []
# for i in range(9):
#     n = int(input())
#     nums.append(n)
#
# n = len(nums)
#
# for i in range(1<<n):
#     lst = []
#     for j in range(n):
#         if i & (1<<j):
#             lst.append(nums[j])
#     if sum(lst) == 100 and len(lst) == 7:
#         for k in sorted(lst):
#             print(k)
#         break

nums = []
for i in range(4):
    n = int(input())
    nums.append(n)

n = len(nums)

for i in range(1<<n):
    lst = []
    print(i)
    for j in range(n):
        print(j)
        if i & (1<<j):
            lst.append(nums[j])
    print(lst)