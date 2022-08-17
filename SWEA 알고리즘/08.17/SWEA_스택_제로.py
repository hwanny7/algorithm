

for t in range(1, int(input())+1):
    N = int(input())
    stack = [0] * N
    top = -1

    for num in list(map(int, input().split())):
        if num == 0 and top != -1:
            stack[top] = 0
            top -= 1

        else:
            top += 1
            stack[top] = num

    max = 0
    for i in stack:
        max += i
    print(f'#{t}', max)

