

for t in range(1, int(input()) + 1):
    H, W = map(int, input().split())

    arr = [[0] * W for _ in range(H)]

    cnt = 1
    for h in range(H):
        for w in range(W):
            arr[h][w + (W - 1 - 2 * w) * (h % 2)] = cnt
            cnt += 1
    print(f'#{t}')
    for i in arr:
        print(*i)
