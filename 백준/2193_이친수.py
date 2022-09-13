def fibo(N):
    if arr[N] != 0:
        return arr[N]
    arr[N] = fibo(N - 2) + fibo(N - 1)
    return arr[N]

N = int(input())
arr = [0] * (N + 1)
arr[0] = 1
arr[1] = 1
print(fibo((N - 1)))

