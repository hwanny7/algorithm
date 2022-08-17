for t in range(1, int(input())+1):
    n, k = map(int, input().split())
    total_count = 0
    lst = list(range(1, 13))
    for i in range(1<<len(lst)):
        total = 0
        count = 0
        for j in range(len(lst)):
            if i & (1<<j):
                total += lst[j]
                count += 1
        if total == k and count == n:
            total_count += 1

    print(f'#{t}', total_count)
