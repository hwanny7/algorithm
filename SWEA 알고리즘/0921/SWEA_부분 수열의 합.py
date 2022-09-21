def find(total, i):
    global cnt
    if total == K:
        cnt += 1
        return
    for j in range(i, N):
        if K < total + arr[j]:
            return
        total += arr[j]
        find(total, j + 1)
        total -= arr[j]


for t in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    cnt = 0
    find(0, 0)
    print(f'#{t}', cnt)

# =======================================================
# def find(total, i):
#     global cnt
#     if total == K:
#         cnt += 1
#         return
#     for j in range(i, N):
#         if K < total + arr[j]:
#             continue
#         total += arr[j]
#         find(total, j + 1)
#         total -= arr[j]
#
#
# for t in range(1, int(input()) + 1):
#     N, K = map(int, input().split())
#     arr = list(map(int, input().split()))
#     cnt = 0
#     find(0, 0)
#     print(f'#{t}', cnt)