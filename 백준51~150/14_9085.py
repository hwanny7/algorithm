
for t in range(int(input())):
    n = int(input())
    total = 0
    nums = list(map(int, input().split()))
    for i in nums:
        total += i
    print(total)