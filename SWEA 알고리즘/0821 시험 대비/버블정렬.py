
#버블정렬
# nums = [5, 3, 2, 10, 100, 44]
#
# for i in range(len(nums)-1, 0, -1):
#     for j in range(0, i):
#         if nums[j] > nums[j + 1]:
#             nums[j], nums[j + 1] = nums[j + 1], nums[j]
# print(nums)

#카운팅 정렬

# nums = [0, 4, 1, 3, 1, 2, 4, 1]
# count = [0] * 5
# new = [0] * len(nums)
#
# for i in range(0, len(nums)):
#     count[nums[i]] += 1
#
# for i in range(1, len(count)):
#     count[i] = count[i] + count[i - 1]
#
# for i in range(len(nums)):
#     count[nums[i]] -= 1
#     new[count[nums[i]]] = nums[i]
#
# print(new)

# #선택 정렬
# nums = [5, 3, 2, 10, 100, 44]
#
# for i in range(len(nums) - 1):
#     min_index = i
#     for j in range(i+1, len(nums)):
#         if nums[j] < nums[min_index]:
#             min_index = j
#     nums[min_index], nums[i] = nums[i], nums[min_index]
# print(nums)

