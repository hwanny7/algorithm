def dik():
    INF = 999999999999
    U = [0] * N
    D = [INF] * N
    D[0] = 0

    for _ in range(N):
        minV = INF
        idx = 0
        for i in range(N):
            if U[i] == 0 and minV > D[i]:
                minV = D[i]
                idx = i

        U[idx] = 1

        for j in range(N):
            if U[j] == 0:
                D[j] = min(D[j], ((path_1[idx] - path_1[j]) ** 2 + (path_2[idx] - path_2[j]) ** 2) *tax)


    print(f'#{t}', round(sum(D)))

for t in range(1, int(input()) + 1):
    N = int(input())
    path_1 = list(map(int, input().split()))
    path_2 = list(map(int, input().split()))
    tax = float(input())
    dik()




