def partition(l, r):
    x = arr[r]
    j = l - 1
    for i in range(l, r):
        if arr[i] <= x:
            j += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[j + 1], arr[r] = arr[r], arr[j + 1]
    return j + 1

def quick_sort(l, r):
    if l < r:
        s = partition(l, r)
        quick_sort(l, s - 1)
        quick_sort(s + 1, r)


for t in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(0, N - 1)
    print(f'#{t}', arr[N // 2])