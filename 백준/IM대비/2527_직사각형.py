for i in range(4):
    x, y, x1, y1, r, c, r1, c1 = map(int, input().split())

    lst = [[x,y,1], [x1, y1, 1], [r, c, 2], [r1, c1, 2]]
    lst.sort()
    # print(lst)
    if lst[1][2] == lst[2][2]:
        if lst[2][1] >= lst[3][1] and lst[3][1] != lst[2][0]:
            print('a')
        elif lst[2][1] <= lst[3][1]:
            print('a')
    elif lst[1][2] != lst[2][2] and lst[1][2] != lst[0][2] and lst[2][1] < lst[1][1]:        #겹쳐서 작은 사각형 생길 때
        if lst[2][0] - lst[1][0] != lst[2][1] - lst[1][1]:
            print('a')
    elif len(set([(x,y),(x1, y1), (r, c), (r1, c1)])) == 3:
        print('c')
    elif len(set([x, x1, r, r1])) + len(set([y, y1, c, c1])) == 7:
        print('b')
    else:
        print('d')
