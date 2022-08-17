for t in range(1, int(input())+1):
    n = int(input())
    nums = list(map(int, input().split()))
    max = nums[0] + nums[1]
    for i in range(2, n):
        if nums[i]+nums[i-1] > max:
            max = nums[i]+nums[i-1]
    print(f'#{t}', max)
