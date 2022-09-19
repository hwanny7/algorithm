for i in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    loop = []
    while True:
        lst = []
        for i in range(N):
            lst.append(abs(arr[i] - arr[(i + 1) % N]))
        arr = lst
        if sum(arr) == 0:
            print('ZERO')
            break
        elif arr in loop:
            print('LOOP')
            break
        loop.append(arr)