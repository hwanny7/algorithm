for t in range(1, int(input()) + 1):
    n = list(map(int, input()))
    temp = [0] * len(n)
    cnt = 0
    for i in range(len(n)):
        if temp[i] != n[i]:
            cnt += 1
            for j in range(i, len(n)):
                temp[j] = n[i]

    print(f'#{t}', cnt)