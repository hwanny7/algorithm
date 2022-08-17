

for t in range(1, int(input())+1):
    n = input()
    stack = [0] * len(n)
    top = -1

    for j in n:
        if j == '{' or j == '(':
            top += 1
            stack[top] = j
        elif j == '}':
            if stack[top] == '{':
                top -= 1
            else:
                print(f'#{t}', 0)
                break
        elif j == ')':
            if stack[top] == '(':
                top -= 1
            else:
                print(f'#{t}', 0)
                break
    else:
        if top < 0:
            print(f'#{t}', 1)
        else:
            print(f'#{t}', 0)

