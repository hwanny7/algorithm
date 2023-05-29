def permutation(lst=[]):
    if len(lst) == N:
        print(*lst)
        return

    for i in range(N):
        if not visit[i]:
            visit[i] = 1
            permutation(lst + [arr[i]])
            visit[i] = 0




N = int(input())
visit = [0] * N
arr = [i for i in range(1, N + 1)]

permutation()
