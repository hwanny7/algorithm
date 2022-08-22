

for t in range(int(input())):

    arr = [list(map(int, input().split())) for _ in range(9)]
    ans = 0

    for i in range(9):
        r = [0] * 9
        c = [0] * 9
        for j in range(9):
            r[arr[i][j] - 1] += 1
            c[arr[j][i] - 1] += 1
        for k in range(9):
            if r[k] == 0:
                ans += 1
                break
            if c[k] == 0:
                ans += 1
                break

    for i in range(0, 9, 3):        # 행
        for j in range(0, 9, 3):    # 열
            check = [0] * 9
            for c in range(i, i + 3):
                for r in range(j, j + 3):
                    check[arr[c][r] - 1] += 1
            for k in range(9):
                if check[k] == 0:
                    ans += 1
                    break

    if ans:
        print(f'#{t + 1}', 0)
    else:
        print(f'#{t + 1}', 1)
