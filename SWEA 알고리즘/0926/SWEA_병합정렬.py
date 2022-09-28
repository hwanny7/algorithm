
def merge_sort(arr, l, h):
    global cnt
    if h - l == 1:
        return arr[l:h], 1
    mid = (l + h) // 2
    l, l_long = merge_sort(arr, l, mid)
    r, r_long = merge_sort(arr, mid, h)

    if l[l_long - 1] > r[r_long - 1]:
        cnt += 1

    ret = []

    l_idx = 0
    r_idx = 0

    while l_idx < l_long and r_idx < r_long:
        if l[l_idx] <= r[r_idx]:
            ret.append(l[l_idx])
            l_idx += 1
        else:
            ret.append(r[r_idx])
            r_idx += 1

    ret += r[r_idx:] + l[l_idx:]

    return ret, l_long + r_long


for t in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr, long = merge_sort(arr, 0, N)
    print(f'#{t}', arr[N // 2], cnt)