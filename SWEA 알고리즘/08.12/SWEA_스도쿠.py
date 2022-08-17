for t in range(1, int(input())+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    result = 0
    for c in range(0, 7, 3):
        for r in range(0, 7, 3):
            num = [0]*9
            for i in range(c, c+3):
                for j in range(r, r+3):
                    if num[arr[i][j]-1] == 0:
                        num[arr[i][j]-1] += 1
                    else:
                        result += 1
    for i in range(9):
        num = [0] * 9
        num1 = [0] * 9
        for j in range(9):
            if num1[arr[j][i]-1] == 0 and num[arr[i][j]-1] == 0:
                num[arr[i][j]-1] += 1
                num1[arr[j][i]-1] += 1
            else:
                result += 1
    if result == 0:
        print(f'#{t}', 1)
    else:
        print(f'#{t}', 0)