

for i in range(int(input())):
    x, y = input().split()
    for j in range(len(y)):
        if j != int(x) -1:
            print(y[j], end='')
    print()
