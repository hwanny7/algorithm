def ans(K, B):
    if K == M:
        print(*arr)
        return
    for i in range(B, N + 1):
        arr[K] = i
        ans(K + 1, i)

N, M = map(int, input().split())
arr = [0] * M
ans(0, 1)
