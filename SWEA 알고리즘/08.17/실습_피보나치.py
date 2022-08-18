# def fibo(n):
#     if n < 2:
#         return n
#
#     else:
#         return fibo(n-1) + fibo(n-2)
#
# for i in range(18):
#     print(i, fibo(i))      #중복 호출로 인해 느림


def fibo(n):
    if memo[n] == -1:  #계산된 적 없음을 나타냄
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

memo = [-1]*101
memo[0] = 0
memo[1] = 1

print(fibo(10))


