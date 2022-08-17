
for k in range(1, int(input())+1):
    N = int(input())
    nums = list(map(int, input().split()))

    for j in range(N-1, 0, -1):
        for i in range(j):
            if nums[i] > nums[i+1]:
                nums[i],nums[i+1] = nums[i+1], nums[i]
    print(f'#{k}', *nums)