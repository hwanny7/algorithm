

for i in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    print((max(nums)-min(nums)) * 2)