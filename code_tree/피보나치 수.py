def fibo(num):
    if arr[num]:
        return arr[num]

    arr[num] = fibo(num -1) + fibo(num - 2)
    return arr[num]


N = int(input())
arr = [0] * 45
arr[0], arr[1] = 1, 1
print(fibo(N - 1))
