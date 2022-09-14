def Tree(L):
    if not L <= N:
        return 0
    left = Tree(L * 2)
    right = Tree(L * 2 + 1)
    return left + right + V[L]


for t in range(1, int(input()) + 1):
    N, M, L = map(int, input().split())

    V = [0] * (N + 1)

    for i in range(M):
        idx, num = map(int, input().split())
        V[idx] = num

    print(f'#{t}', Tree(L))