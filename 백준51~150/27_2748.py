def P(a, b, t):
    if t == 1:
        return b
    else:
        return P(b, a+b, t-1)

n = int(input())
print(P(0, 1, n))

