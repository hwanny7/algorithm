def inorder(v):
    global lst
    if v == 0:
        return

    inorder(L[v])

    lst += P[v]
    inorder(R[v])

for t in range(1, 11):
    V = int(input())

    L = [0] * (V + 1)
    R = [0] * (V + 1)
    P = [0] * (V + 1)
    for i in range(V):
        temp = input().split()
        if len(temp) == 4:
            P[int(temp[0])] = temp[1]
            L[int(temp[0])] = int(temp[2])
            R[int(temp[0])] = int(temp[3])
        elif len(temp) == 3:
            P[int(temp[0])] = temp[1]
            L[int(temp[0])] = int(temp[2])
        else:
            P[int(temp[0])] = temp[1]


    lst = ''

    inorder(1)

    print(f'#{t}', lst)