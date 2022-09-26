

def cost(K, total, visit):
    global ans
    if total >= ans:
        return

    if K == N:
        ans = min(total, ans)
        return

    for i in range(N):
        if not visit & (1 << i):
            cost(K + 1, total + arr[K][i], visit | (1 << i))


for t in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 15 * 100
    cost(0, 0, 0)
    print(f'#{t}', ans)