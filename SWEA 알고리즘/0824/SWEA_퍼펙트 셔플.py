
for t in range(1, int(input()) + 1):
    N = int(input())
    S = input().split()

    if N % 2:
        m = N // 2 + 1
    else:
        m = N // 2

    print(f'#{t}', end = ' ')
    for i in range(m):
        print(S[i], end =' ')
        if not i + m >= N:
            print(S[i + m], end = ' ')
    print()
