
N = int(input())

memo = [0] * 1001
memo[1] = 2
memo[2] = 7


for i in range(3, N + 1):
    if i % 2:
        memo[i] = memo[i - 1] * 2
    else:
        memo[i] = memo[i - 2] * 2 + 3

print(memo)