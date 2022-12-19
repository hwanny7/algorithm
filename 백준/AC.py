for t in range(int(input())):
    command = input()
    N = int(input())
    arr = input()[1:-1].split(',')
    status = True
    front = -1
    back = N - 1

    ans = False
    for i in command:
        if i == 'D':
            if status:
                front += 1
            else:
                back -= 1

            if front > back:
                ans = not ans
                break
        else:
            status = not status

    if ans:
        print('error')
    elif status:
        print('['+','.join(arr[front + 1:back + 1])+']')
    else:
        print('['+ ','.join(arr[front + 1:back + 1][::-1]) +']')
