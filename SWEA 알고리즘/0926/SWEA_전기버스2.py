def find(station, idx, cnt):
    global ans

    next = station[idx] + idx
    if cnt >= ans:
        return

    if next >= N:
        ans = min(cnt, ans)
        return

    find(station, next, cnt + 1)
    for i in range(next - 1, idx, -1):
        if station[i] > station[next]:
            find(station, i, cnt + 1)

for t in range(1, int(input()) + 1):
    station = list(map(int, input().split()))
    N = station[0]
    ans = 101
    find(station, 1, 0)
    print(f'#{t}', ans)



# def find(gas, idx, cnt):
#     global ans
#
#     if cnt >= ans:
#         return
#
#     if gas + idx >= N:
#         ans = min(cnt, ans)
#         return
#
#     V = idx
#     next = gas + idx
#     find(station[next], next, cnt + 1)
#     for i in range(next - 1, idx, -1):
#         if station[i] > station[next]:
#             find(station[i], i, cnt + 1)
#
# for t in range(1, int(input()) + 1):
#     station = list(map(int, input().split()))
#     N = station[0]
#     ans = 101
#     find(station[1], 1, 0)
#     print(f'#{t}', ans)
