def T(x):
    if arr[x] != -1:
        return arr[x]
    arr[x] = T(x - 2) * 2 + T(x - 1)
    return arr[x]

while True:
    try:
        N = int(input())
        arr = [1, 1, 3]
        arr += [-1] * (N - 2)
        print((T(N)))
    except:
        break