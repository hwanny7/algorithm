


for i in range(int(input())):
    lst = []
    x, y = input().split()
    for j in range(len(x)):
        if ord(y[j]) >= ord(x[j]):
            lst.append(ord(y[j]) - ord(x[j]))
        else:
            lst.append( 26 + ord(y[j]) - ord(x[j]))
    print('Distances:', *lst)