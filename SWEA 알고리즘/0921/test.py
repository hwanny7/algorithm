def find(idx, cnt):
    global grand
    global cn
    cn += 1
    if cnt == K or idx == l:
        total = 0
        for i in range(l):
            total += arr[i] * 10 ** (l - 1 - i)
        if (K - cnt) % 2:
            total += arr[-1] * 10 + arr[-2] - arr[-2] * 10 - arr[-1]
        if grand < total:
            grand = total
        return

    for i in range(l):
        if i == idx:
            continue

        if arr[idx] == arr[i] and i < idx:
            find(idx + 1, cnt + 1)
        elif arr[idx] <= arr[i] and idx < i:
            arr[idx], arr[i] = arr[i], arr[idx]
            find(idx + 1, cnt + 1)
            arr[idx], arr[i] = arr[i], arr[idx]

    else:
        find(idx + 1, cnt)


for tc in range(1, int(input()) + 1):
    arr, K = input().split()
    arr = list(map(int, arr))
    K = int(K)
    l = len(arr)
    grand = 0
    cn = 0
    find(0, 0)

    print(f'#{tc}', grand, cn)