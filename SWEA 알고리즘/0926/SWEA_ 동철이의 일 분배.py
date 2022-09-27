def back(K, total, used, lst = []):
    global ans
    if ans >= total:
        return
    if K == N:
        ans = max(ans, total)
        return

    for i in range(N):
        if used & (1 << i) == 0:
            back(K + 1, total * (arr[K][i] / 100), used | (1 << i), lst + [arr[K][i]])


for t in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 1
    for i in range(N):
        for j in range(N):

    back(0, 100, 0)
    print(f'#{t} {ans:.6f}')

