

for i in range(int(input())):

    n = input()
    stack = [0] * len(n)
    top = -1

    for i in n:
        if i == '(':
            top += 1
            stack[top] = i
        else:
            if top < 0:
                print('NO')
                break
            elif stack[top] == '(':
                top -= 1
            else:
                print('N0')
                break
    else:
        if top > -1:
            print('NO')
        else:
            print('YES')
