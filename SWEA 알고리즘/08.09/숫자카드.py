for i in range(1, int(input())+1):
    n = int(input())
    nums = input()
    arr = [0] * 10

    for j in range(len(nums)):
        arr[int(nums[j])] += 1

    max = 0
    count = 0
    for k in range(len(arr)):
        if arr[k] >= count:
            count = arr[k]
            max = k
    print(f'#{i}', max, count)