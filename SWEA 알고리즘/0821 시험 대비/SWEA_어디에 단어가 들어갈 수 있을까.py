

for t in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)]
    arr.append([0] * (N + 1))

    ans = 0

    for c in range(N + 1):
        total = total2 = 0
        for r in range(N + 1):
            if arr[c][r] == 1:
                total += 1
            else:
                if total == K:
                    ans += 1
                total = 0       #변수 초기화
            if arr[r][c] == 1:
                total2 += 1
            else:
                if total2 == K:
                    ans += 1
                total2 = 0

    print(f'#{t}', ans)
