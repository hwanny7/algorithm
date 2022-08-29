import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

for i in range(1, N):
    nums[i] = nums[i] + nums[i - 1]

for i in range(M):
    f, l = map(int, input().split())
    if f != 1:
        print(nums[l - 1] - nums[f - 2])
    else:
        print(nums[l - 1])
