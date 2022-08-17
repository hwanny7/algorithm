
for t in range(1, int(input())+1):
    n = int(input())
    nums = list(map(int, input().split()))

    max = 0
    min = 0
    for i in range(1, n):
        if nums[max] <= nums[i]:
            max = i
        elif nums[min] > nums[i]:
            min = i
    print(f'#{t}', abs((max-1)-(min-1)))
