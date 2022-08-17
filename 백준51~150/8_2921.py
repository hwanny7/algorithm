


n = int(input())

total = 0
for i in range(n+1):
    for j in range(n+1):
        if i == j:
            total += i+j
            print(i, j)
        elif j > i:
            total += i+j
            print(i, j)

print(total)

