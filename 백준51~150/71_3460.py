
for i in range(int(input())):
    n = int(input())

    lst = []
    while True:
        if n == 1:
            lst.append(1)
            break
        else:
            lst.append(n % 2)
            n //= 2
    for j in range(len(lst)):
        if lst[j] == 1:
            print(j, end=' ')