

for i in range(1, int(input())+1):
    nums = list(map(int, input().split()))
    nums = nums[1:]
    nums.sort(reverse=True)
    max = 0
    for j in range(1, len(nums)):
        if max < nums[j-1]-nums[j]:
            max = nums[j-1]-nums[j]
    print(f'Class {i}')
    print(f'Max {nums[0]}, Min {nums[-1]}, Largest gap {max}')