
def perm(k, N):
    global min

    total1 = 0
    for j in range(k):
        total1 += arr1[j][arr[j]]
    if total1 >= min:
        return

    if k == N:
        total = 0
        for j in range(len(arr)):
            total += arr1[j][arr[j]]
        if total < min:
            min = total
        return
    else:
        for i in range(k, N):
            arr[k], arr[i] = arr[i], arr[k]
            perm(k + 1, N)
            arr[k], arr[i] = arr[i], arr[k]


for t in range(1, int(input()) + 1):
    N = int(input())
    arr1 = [list(map(int, input().split())) for _ in range(N)]
    arr = []
    for i in range(N):
        arr.append(i)
    min = 1000
    perm(0, N)
    print(f'#{t}', min)

