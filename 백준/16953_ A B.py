

X, Y = map(int, input().split())

count = 1
while X != Y:
    if X > Y:
        count = -1
        break
    if Y % 10 == 1:
        Y //= 10
    else:
        Y /= 2
    count += 1
print(count)