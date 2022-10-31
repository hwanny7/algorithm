for t in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    Big = max(arr)
    total = 0
    one = 0
    for i in range(N):
        total += Big - arr[i]
        if (Big - arr[i]) % 2:
            one += 1

    if one * 3 > total:
        print(f'#{t}', one * 2 - 1)
    else:
        print(f'#{t}', (total // 3) * 2 + (total % 3))
#

for T in range(1, int(input()) + 1):
    N = int(input())
    a = list(map(int, input().split()))
    B = max(a)
    t = 0
    o = 0
    for i in range(N):
        s = B - a[i]
        t += s
        if s % 2:
            o += 1

    print(f'#{T}', o * 2 - 1 if o * 3 > t else (t // 3) * 2 + (t % 3))