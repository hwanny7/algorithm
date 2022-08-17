for i in range(1, int(input())+1):
    n = int(input())
    nums = list(map(int, input().split()))
    max = 0
    min = 0
    for j in range(1, n):
        if nums[j] >= nums[max]:
            max = j
        elif nums[j] < nums[min]:
            min = j
    if max > min:
        print(f'#{i}', abs(max-min))
    else:
        print(f'#{i}', abs(min-max))