
N = int(input())

dp = [0] * (N + 1)
dp[0] = 1

for i in range(N + 1):
    if not dp[i]:
        continue

    if i + 2 <= N:
        dp[i + 2] += dp[i]

    if i + 3 <= N:
        dp[i + 3] += dp[i]

print(dp[-1])