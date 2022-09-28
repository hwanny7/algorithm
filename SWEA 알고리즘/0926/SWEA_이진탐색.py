def find(lst, l, r, key, before):

    if not l <= r:
        return 0

    mid = (l + r) // 2
    if lst[mid] == key:
        return 1
    elif lst[mid] > key:
        if before == 1:
            return 0
        return find(lst, l, mid - 1, key, 1)
    else:
        if before == 0:
            return 0
        return find(lst, mid + 1, r, key, 0)


for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    arr2 = list(map(int, input().split()))
    ans = 0
    for i in arr2:
        ans += find(arr, 0, N - 1, i, -1)

    print(f'#{t}', ans)

