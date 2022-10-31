
N, M = map(int, input().split())        #N줄, M개
arr = [list(map(int, input())) for _ in range(N)]

for i in range(1, N):
    if arr[i - 1][0] and arr[i][0]:
        arr[i][0] = arr[i][0] + arr[i - 1][0]

for i in range(1, M):
    if arr[0][i - 1] and arr[0][i]:
        arr[0][i] = arr[0][i] + arr[0][i - 1]



for i in arr:
    print(i)
