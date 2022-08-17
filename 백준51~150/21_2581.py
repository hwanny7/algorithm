M, N = map(int, input().split())

for i in range(M, N+1):
    for j in range(2, i+1):
        if i % j == 0 and i != 2:
            break
        elif j ** 2 > i:
            print(i)
            break