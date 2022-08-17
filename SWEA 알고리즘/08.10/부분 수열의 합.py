for t in range(1, int(input())+1):
    n, x = map(int, input().split())
    arr= list(map(int, input().split()))

    count = 0
    for i in range(1<<n):
        total = 0
        for j in range(n):
            if i & (1<<j):
                total += arr[j]
        if total == x:
            count += 1

    print(f'#{t}', count)