

for t in range(1, int(input())+1):

    n = input()
    stack = [0] * len(n)
    top = -1

    for i in n:
        if i == stack[top]:     # -1은 끝을 의미하니까 인덱스 오류가 나지 않는다.
            top -= 1
        else:
            top += 1
            stack[top] = i

    print(f'#{t}', len(stack[:top+1]))
