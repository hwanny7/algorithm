for i in range(1, int(input())+1):
    n = int(input())
    nums = list(map(int, input().split()))
    min = nums[0]
    max = nums[0]
    for j in range(1, n):
        if nums[j] > max:
            max = nums[j]
        elif nums[j] < min:
            min = nums[j]

    print(f'#{i}', max - min)
