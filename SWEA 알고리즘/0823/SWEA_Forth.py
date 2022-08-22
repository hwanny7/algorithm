def push(x):
    global top
    top += 1
    stack[top] = x

def pop():
    global top
    top -= 1
    return stack[top + 1]

def verify(i):
    if i == '-' or i == '+' or i == '*' or i =='/':
        return 1
    else:
        return 0


for t in range(1, int(input()) + 1):
    S = input().split()
    stack = [0] * len(S)
    top = -1

    for i in range(len(S) - 1):
        if S[i] == '-':
            num1, num2 = pop(), pop()
            push(num2 - num1)
        elif S[i] == '+':
            num1, num2 = pop(), pop()
            push(num2 + num1)
        elif S[i] == '*':
            num1, num2 = pop(), pop()
            push(num2 * num1)
        elif S[i] == '/':
            num1, num2 = pop(), pop()
            push(num2 / num1)
        else:
            push(int(S[i]))

    if top != -1:
        print(f'#{t}', stack[0])
    else:
        print(f'#{t} error')