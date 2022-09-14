def Tree(v):
    if not v:
        return 0

    l = Tree(left[v])
    r = Tree(right[v])

    return l + r + 1



for t in range(1, int(input()) + 1):
    E, start = map(int, input().split())
    left = [0] * (E + 2)
    right = [0] * (E + 2)
    arr = list(map(int, input().split()))
    for i in range(0, E * 2, 2):
        if left[arr[i]] == 0:
            left[arr[i]] = arr[i + 1]
        else:
            right[arr[i]] = arr[i + 1]

    print(f'#{t}', Tree(start))