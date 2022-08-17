import sys; sys.stdin = open('특별한 정렬.txt')

for t in range(1, int(input())+1):
    n = int(input())
    nums = list(map(int, input().split()))

    for i in range(n-1):
        max = i
        for j in range(i+1, n):
            if i % 2 == 0:       # 짝수일 때 최대
                if nums[max] < nums[j]:
                    max = j
            else:
                if nums[max] > nums[j]:
                    max = j
        nums[i], nums[max] = nums[max], nums[i]
    print(f'#{t}', end=' ')
    for k in range(10):
        print(nums[k], end=' ')
    print()

