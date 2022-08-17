def binary(i):
    start = 0
    end = n-1

    while start <= end:
        middle = (start+end) // 2
        if nums[middle] == i:
            return 1
        elif nums[middle] > i:
            end = middle - 1
        else:
            start = middle + 1
    return 0


n = int(input())
nums = list(map(int, input().split()))
nums.sort()
m = int(input())
nums2 = list(map(int, input().split()))

for i in nums2:
    print(binary(i))