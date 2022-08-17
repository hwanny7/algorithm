import sys

for t in range(10):
    T = int(input())
    arr = []
    for i in range(100):
        temp = list(map(int, input().split()))
        arr.append(temp)

    # for i in range(1, 101):
    #     lst = []
    #     for j in range(i*100-100,i*100):
    #         lst.append(temp[j])
    #     arr.append(lst)
    # print(arr)

    r = 0
    c = 0
    cross1 = 0
    cross2 = 0

    for i in range(100):
        r_max = 0
        c_max = 0
        cross1 += arr[i][i]
        cross2 += arr[i][99-i]
        for j in range(100):
            r_max += arr[i][j]
            c_max += arr[j][i]

        if r_max > r:
            r = r_max
        if c_max > c:
            c = c_max
    max = 0
    for k in [r, c, cross1, cross2]:
        if k > max:
            max = k
    print(f'#{T}', max)



