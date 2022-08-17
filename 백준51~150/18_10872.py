
def P(n):
    while True:
        if n == 0:
            return 1
        else:
            return n * P(n-1)

print(P(int(input())))
