for t in range(1, 11):
    N = int(input())        # 1은 N극, 2는 S극 (테이블 위 N극, 아래 S극)
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for i in range(N):
        condition = 0
        for j in range(N):
            if arr[j][i] == 2:
                if condition == 1:
                    cnt += 1
                    condition = 0
            elif arr[j][i] == 1:        #컨디션 > 1
                condition = 1
    print(f'#{t}', cnt)