import sys
sys.setrecursionlimit(1000100)
input = sys.stdin.readline

def fibo(x):
    if x <= 1:
        return arr[x]
    elif arr[x]:
        return arr[x]
    else:
        arr[x] = fibo(x - 1) + fibo(x - 2)
        return arr[x]

n = int(input())
arr = [0, 1] + [0] * (n - 1)
print(fibo(n))