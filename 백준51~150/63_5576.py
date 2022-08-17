
nums = []
for i in range(10):
    n = int(input())
    nums.append(n)

nums2 = []
for i in range(10):
    n = int(input())
    nums2.append(n)

print(sum(sorted(nums)[-3:]), sum(sorted(nums2)[-3:]) )
