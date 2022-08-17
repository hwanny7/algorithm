import sys; sys.stdin = open('연속한 1의 개수.txt')

for t in range(1, int(input())+1):
    n = int(input())
    nums = list(map(int, input().split())) + [0]

    final_total = 0
    total = 1
    for i in range(1, n+1):
        if nums[i] > nums[i-1]:
            total += 1
        else:
            if final_total < total:
                final_total = total
                total = 1

    print(f'#{t}', final_total)









