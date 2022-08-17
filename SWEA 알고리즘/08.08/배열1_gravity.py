
for m in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))

    arr_lst = []
    for j in range(len(arr)-1):
        total = 0
        for k in arr[j+1:]:
            if arr[j] > k:
                total += 1
        arr_lst.append(total)

    print(f'#{m}', max(arr_lst))