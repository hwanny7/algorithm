

while True:
    str = input()
    if len(str) == 1 and str[0] == '.':
        break
    stack = []
    ans = 0

    for i in str:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                ans += 1
                break
            elif stack.pop() != '(':
                ans += 1
                break
        elif i == ']':
            if len(stack) == 0:
                ans += 1
                break
            elif stack.pop() != '[':
                ans += 1
                break

    if 0 < ans or len(stack) != 0:
        print('no')
    else:
        print('yes')