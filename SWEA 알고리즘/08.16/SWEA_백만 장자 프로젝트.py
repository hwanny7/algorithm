

for t in range(1, int(input())+1):
    l = int(input())
    nums = list(map(int, input().split()))
    total = 0
    max = l - 1
    for i in range(l-2, -1, -1):
        if nums[max] > nums[i]:
            total += nums[max] - nums[i]
        else:
            max = i
    print(f'#{t}', total)