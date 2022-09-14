for i in range(1, int(input()) + 1):
    N, P = map(int, input().split())
    plus = N % P
    print(f'#{i}', (N // P + 1) ** plus * (N // P) ** (P - plus))