for t in range(1, int(input()) + 1):
    N, num = input().split()
    ans = []
    N = int(N)
    print(f'#{t} ', end='')
    for i in range(N):
        a = int(num[i], 16)
        ans = format(a, 'b')
        print('0' * (4 - len(ans)) + ans, end='')
    print()
