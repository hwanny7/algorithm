N, M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]

ans = 0
useless = 0

for i in range(N):
    for j in range(M):
        if not arr[i][j]:
            continue

        if i == 0 or j == 0:
            useless = 0

        else:
            change = min(arr[i - 1][j - 1], arr[i - 1][j], arr[i][j - 1]) + 1
            arr[i][j] = change

        if ans < arr[i][j]:
            ans = arr[i][j]

print(ans ** 2)



