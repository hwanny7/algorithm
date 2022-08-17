import sys; sys.stdin = open('파리 퇴치.txt')

for t in range(1, int(input())+1):
    N, M = map(int, input().split())

    nums = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N-M):
        print('i입니다', i)
        for j in range(i, i+M-1):
            print(j)









    # dr = [0, 0, 0, -1, 1, 1, 1, -1, -1]
    # dc = [0, -1, 1, 0, 0, -1, 1, 1, -1]
    #
    # grand_total = 0



    # for c in range(1, N-1):
    #     for r in range(1, N-1):
    #         total = 0
    #         for i in range(9):
    #             total += nums[c+dc[i]][r+dr[i]]
    #         if grand_total < total:
    #             grand_total = total
    #
    # print(f'#{t}', grand_total)




