
for t in range(1, int(input())+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))

    for i in range(N-1):
        min = i
        for j in range(i+1, N):
            if lst[min] > lst[j]:
                min = j
        lst[i], lst[min] = lst[min], lst[i]

    print(f'#{t}', list(set(lst))[K-1])
