

N, K = map(int, input().split())

arr = list(map(int, input().split()))

cnt = 0
box = []
for i in range(N-1, 0, -1):
    for j in range(0, i):
        if arr[j + 1] < arr[j]:
            arr[j + 1], arr[j] = arr[j], arr[j + 1]
            cnt += 1
            if cnt == K:
                box = [arr[j], arr[j + 1]]

if cnt < K:
    print(-1)
else:
    print(*box)