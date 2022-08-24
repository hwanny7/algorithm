
for t in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    times = list(map(int, input().split()))
    times.sort()
    total = 0

    for i in range(N):
        if not (times[i] // M * K) - i >= 1:
            print(f'#{t} Impossible')
            break
    else:
        print(f'#{t} Possible')