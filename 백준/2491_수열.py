
n = int(input())

nums = list(map(int,input().split())) + [0]
nums2 = nums[:-1] +[1000]

max = 0
count = 1
count2 = 1
for i in range(n):
    if nums[i] <= nums[i+1]:
        count += 1
    else:
        if max < count:
            max = count
        count = 1

    if nums2[i] >= nums2[i+1]:
        count2 += 1

    else:
        if max < count2:
            max = count2
        count2 = 1

print(max)
