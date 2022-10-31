

switch = int(input())

nums = list(map(int, input().split()))

person = int(input())

for p in range(person):

    x, num = map(int, input().split())
    if x == 1:
        for i in range(len(nums)):
            if (i + 1) % num == 0:
                if nums[i]:
                    nums[i] = 0
                else:
                    nums[i] = 1
    else:
        if nums[num-1]:
            nums[num-1] = 0
        else:
            nums[num-1] = 1
        k = 1
        while True:
            if 0 <= num-1-k < switch and 0 <= num-1+k < switch and nums[num-1-k] == nums[num-1+k]:
                if nums[num-1-k]:
                    nums[num-1-k] = nums[num-1+k] = 0
                else:
                    nums[num - 1 - k] = nums[num - 1 + k] = 1
                k += 1
            else:
                break

for i in range(switch):
    if (i + 1) % 20 == 0:
        print(nums[i], end=' ')
        print()
    else:
        print(nums[i], end=' ')

