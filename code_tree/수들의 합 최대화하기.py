def permutation(k, total, used):
    global ans
    if k == N:
        ans = max(ans, total)
        return

    for i in range(N):
        if used & (1 << i):
            continue
        permutation(k + 1, total + arr[k][i], used | (1 << i))





N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
permutation(0, 0, 0)
print(ans)
