def v(n):
    if n == '+':
        return 1
    elif n == '*':
        return 2
    else:
        return 0


def r(a, b, n):
    if n == '*':
        return a * b
    elif n == '+':
        return a + b

for t in range(1, 11):

    N = int(input())
    S = input()
    stack = [0] * N
    top = -1
    nums = []

    for i in S:
        if not v(i):
            nums.append(int(i))
        else:
            while True:
                if v(stack[top]) >= v(i):
                    nums.append(stack[top])
                    top -= 1
                else:
                    top += 1
                    stack[top] = i
                    break

    else:
        if top != -1:
            for i in range(top, -1, -1):
                nums.append(stack[i])
        top = -1


    for i in nums:
        if not v(i):
            top += 1
            stack[top] = i
        else:
            stack[top - 1] = r(stack[top - 1], stack[top], i)
            top -= 1

            
    print(f'#{t}', stack[0])


