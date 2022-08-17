

for i in range(int(input())):
    nums = list(map(int, input().split()))
    nums.remove(max(nums))
    nums.remove(min(nums))
    if max(nums) - min(nums) >= 4:
        print('KIN')
    else:
        print(sum(nums))