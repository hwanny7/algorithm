# for t in range(1, int(input())+1):
#     n = int(input())
#     arr = [[0]* n for _ in range(n)]
#     dr = [1, 0, -1, 0] * n*n  #우, 좌 (홀수) 하, 상(짝수)
#     dc = [0, 1, 0, -1] * n*n
#
#     r = -1
#     c = 0
#     num = 1
#     i = 0     #dr, dc 움직일 방향키
#
#     while num <= n*n:
#         r += dr[i]
#         c += dc[i]
#
#         if 0 <= r < n and 0 <= c <n:      # 인덱스 범위 넘는지 확인
#             if arr[c][r] == 0:
#                 arr[c][r] += num
#                 num += 1
#             else:                        # 같은 값 부딪혔을 때 인덱스 다시 감소 시키고 방향 바꾸기
#                 r -= dr[i]
#                 c -= dc[i]
#                 i += 1
#         else:                       #인덱스 범위를 넘었을 때는 외곽에 부딪혔을 경우니까 인덱스 위치 원위치 시키고 방향 바꾸기
#             r -= dr[i]
#             c -= dc[i]
#             i += 1
#     print(f'#{t}')
#     for j in arr:
#         print(*j)


# new version
for t in range(1, int(input()) + 1):
    n = int(input())

    arr = [[0] * n for _ in range(n)]

    dr = [1, 0, -1, 0]# 하, 우, 상, 좌
    dc = [0, 1, 0, -1]

    r = -1
    c = 0
    j = 0

    for i in range(1, n*n+1):
        if 0 <= c + dc[j % 4] < n and 0 <= r + dr[j % 4] < n and arr[c + dc[j % 4]][r + dr[j % 4]] == 0:
            arr[c + dc[j % 4]][r + dr[j % 4]] = i
            r = r + dr[j % 4]
            c = c + dc[j % 4]
        else:
            j += 1
            arr[c + dc[j % 4]][r + dr[j % 4]] = i
            r = r + dr[j % 4]
            c = c + dc[j % 4]

    print(f'#{t}')
    for j in arr:
        print(*j)

