def P(x, y, n):
    if n == 0:
        return x
    else:
        n -= 1
        return P(y, x+y, n)



n = int(input())
print(P(0, 1, n))