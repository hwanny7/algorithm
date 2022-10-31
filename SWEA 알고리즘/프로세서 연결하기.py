def change(c, r, i):
    temp_c = c
    temp_r = r
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    flag = arr[c][r]
    wire = 0
    while True:
        c = c + dc[i]
        r = r + dr[i]
        if 0 <= c < N and 0 <= r < N:
            if not arr[c][r]:
                arr[c][r] = flag
                wire += 1
            else:
                de_change(temp_c, temp_r, i)
                return 0, 0
        else:
            return 1, wire


def de_change(c, r, i):
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    flag = arr[c][r]
    while True:
        c = c + dc[i]
        r = r + dr[i]
        if 0 <= c < N and 0 <= r < N:
            if arr[c][r] == flag:
                arr[c][r] = 0
            else:
                return
        else:
            return


def process(P=0, cnt=0, wire=0):
    global ans, long, all
    if all - P + cnt < ans:
        return
    if all - P + cnt == ans and long <= wire:
        return
    if P == len(store):
        if ans < cnt:
            ans = cnt
            long = wire
        elif ans == cnt:
            if long > wire:
                long = wire
        return

    c, r = store[P]
    cc = 0
    for i in range(4):
        n, w = change(c, r, i)
        if n == 0:
            cc += 1
            continue
        process(P + 1, cnt + n, wire + w)
        de_change(c, r, i)
    else:
        if cc == 4:
            process(P + 1, cnt, wire)


for t in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    store = []
    flag = 2
    all = 0
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if arr[i][j]:
                store.append([i, j])
                arr[i][j] = flag
                flag += 1
                all += 1

    ans = 0
    long = 0xffffffffffff
    process()
    print(f'#{t}', long)

# for 문으로 N - 1까지만 가게 하면 조금 낭비를 줄일 수 있을 것 같긴 함


# def change(c, r, i):
#     temp_c = c
#     temp_r = r
#     dr = [0, 0, -1, 1]
#     dc = [-1, 1, 0, 0]
#     flag = arr[c][r]
#     wire = 0
#     while True:
#         c = c + dc[i]
#         r = r + dr[i]
#         if 0 <= c < N and 0 <= r < N:
#             if not arr[c][r]:
#                 arr[c][r] = flag
#                 wire += 1
#             else:
#                 de_change(temp_c, temp_r, i)
#                 return 0, 0
#         else:
#             return 1, wire
#
#
# def de_change(c, r, i):
#     dr = [0, 0, -1, 1]
#     dc = [-1, 1, 0, 0]
#     flag = arr[c][r]
#     while True:
#         c = c + dc[i]
#         r = r + dr[i]
#         if 0 <= c < N and 0 <= r < N:
#             if arr[c][r] == flag:
#                 arr[c][r] = 0
#             else:
#                 return
#         else:
#             return
#
#
# def process(P=0, cnt=0, wire=0):
#     global ans, long, all
#     if all - P + cnt < ans:
#         return
#     if all - P + cnt == ans and long <= wire:
#         return
#     if P == len(store):
#         if ans < cnt:
#             ans = cnt
#             long = wire
#         elif ans == cnt:
#             if long > wire:
#                 long = wire
#         return
#
#     c, r = store[P]
#     cc = 0
#     for i in range(4):
#         n, w = change(c, r, i)
#         if n == 0:
#             cc += 1
#             continue
#         process(P + 1, cnt + n, wire + w)
#         de_change(c, r, i)
#     else:
#         if cc == 4:
#             process(P + 1, cnt, wire)
#
#
# for t in range(1, int(input()) + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     store = []
#     flag = 2
#     all = 0
#     for i in range(1, N - 1):
#         for j in range(1, N - 1):
#             if arr[i][j]:
#                 store.append([i, j])
#                 arr[i][j] = flag
#                 flag += 1
#                 all += 1
#
#     ans = 0
#     long = 0xffffffffffff
#     process()
#     print(f'#{t}', long)