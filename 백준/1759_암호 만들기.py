def find(K, B, I):
    if K == L:
        if I >= 1 and L - I >= 2:
            print(''.join(ans))
        return
    for i in range(B, N):
        ans[K] = alpha[i]
        if alpha[i] in ['a', 'e', 'i', 'o', 'u']:
            find(K + 1, i + 1, I + 1)
        else:
            find(K + 1, i + 1, I)


L, N = map(int, input().split())
ans = [[] for _ in range(L)]
alpha = input().split()
alpha.sort()
find(0, 0, 0)

