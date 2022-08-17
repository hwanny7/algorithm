

for i in range(int(input())):
    nums = list(map(int, input().split()))
    print(sorted(nums, reverse = True)[2])