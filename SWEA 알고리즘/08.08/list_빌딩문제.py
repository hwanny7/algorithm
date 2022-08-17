for i in range(1, 11):
    n = int(input())
    nums = list(map(int, input().split()))
    total = 0
    for j in range(2, n-2):
        if nums[j] > nums[j-1] and nums[j] > nums[j-2]:
            if nums[j] > nums[j+1] and nums[j] > nums[j+2]:
                total += 1
     
    print(f'#{i}', total)