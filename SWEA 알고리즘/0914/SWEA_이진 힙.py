

for t in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    V = [0] * (N + 1)
    for i in range(1, N + 1):
        V[i] = arr[i - 1]
        P = i // 2
        while P and V[i] < V[P]:
            V[i], V[P] = V[P], V[i]
            i = P
            P = P // 2

    total = 0
    while V[N] != 0:
        N = N // 2
        total += V[N]

    print(f'#{t}', total)