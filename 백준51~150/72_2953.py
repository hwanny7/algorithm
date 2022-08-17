
# lst = [0] * 5    #문제 잘못 이해해서 1번 참가자가 2,3,4,5 참가자 순서 매기는 줄 알았음
# for i in range(5):
#     nums = list(map(int, input().split()))
#     for j in range(len(nums)):
#         if i <= j:
#             lst[j+1] += nums[j]
#         else:
#             lst[j] += nums[j]
# print(lst)

lst = []
for i in range(1, 6):
    nums = list(map(int, input().split()))
    lst.append((i, sum(nums)))

max = 0
for i in range(1, len(lst)):
    if lst[max][1] < lst[i][1]:
        max = i
print(*lst[max])