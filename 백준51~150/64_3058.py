

for i in range(int(input())):
    nums = list(map(int, input().split()))
    total = 0
    min = 101
    for j in nums:
        if j % 2 == 0:
            total += j
            if min > j:
                min = j
    print(total, min)

