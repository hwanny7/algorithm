def paper(n):
    if memo[n] == -1:
        memo[n] = paper(n-1) + paper(n-2) * 2
    return memo[n]



for t in range(1, int(input()) + 1):
    n = int(input())
    n = (n // 10) - 1
    memo = [-1] * (n + 1)
    memo[0] = 1
    memo[1] = 3
    print(f'#{t}', paper(n))

