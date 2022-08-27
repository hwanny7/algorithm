for t in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for i in range(N):
        status = 0
        for j in range(N):
            if arr[j][i] == 2 and status:
                cnt += 1
                status = 0
            elif arr[j][i] == 1:
                status = 1
    print(f'#{t}', cnt)