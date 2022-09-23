def find():
    for i in range(l):
        temp = three[i]
        for j in range(3):
            if three[i] != str(j):
                three[i] = str(j)
                if int(''.join(three), 3) in check:
                    return(int(''.join(three), 3))
                three[i] = temp

for t in range(1, int(input()) + 1):
    two = input()
    three = list(input())
    l = len(three)
    check = []
    for i in range(len(two)):
        check.append(int(two, 2) ^ 1 << i)

    print(f'#{t}', find())


