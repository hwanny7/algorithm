def push(x):
    global top
    top += 1
    stack[top] = x

def pop():
    global top
    top -= 1
    return stack[top + 1]

for t in range(1, int(input()) + 1):
    S = input().split()
    stack = [0] * len(S)
    top = -1
    lst = ['-', '+', '/', '*']
    for i in range(len(S) - 1):
        if S[i] not in lst:
            push(int(S[i]))
        else:
            if top < 1:
                print(f'#{t} error')
                break
            else:
                num1, num2 = pop(), pop()
                if S[i] == '-':
                    push(num2 - num1)
                elif S[i] == '+':
                    push(num2 + num1)
                elif S[i] == '*':
                    push(num2 * num1)
                else:
                    push(int(num2 / num1))
    else:
        if top > 0:
            print(f'#{t} error')
        else:
            print(f'#{t}', stack[0])
