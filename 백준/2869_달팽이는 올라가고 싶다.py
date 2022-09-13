import math
A, B, V = map(int, input().split())

if A == V:
    print(1)

elif 0 <= math.ceil((V - A) / (A - B)) < 1:
    print(2)

else:
    print(int(math.ceil((V - A) / (A - B)) + 1))