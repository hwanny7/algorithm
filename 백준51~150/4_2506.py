n = int(input())

nums = list(map(int, input().split()))

total = 0
count = 0
for i in nums:
    if i == 1:
        total += i + count
        count += 1
    else:
        count = 0
print(total)