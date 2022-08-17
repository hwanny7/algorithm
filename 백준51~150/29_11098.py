

for t in range(1, int(input())+1):
    lst = []
    for i in range(int(input())):
        x, y = input().split()
        lst.append((int(x), y))
    max = 0
    for j in range(1, len(lst)):
        if lst[max][0] < lst[j][0]:
            max = j
    print(lst[max][1])

