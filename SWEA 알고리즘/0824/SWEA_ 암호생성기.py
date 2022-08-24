
for t in range(1, 11):
    T = int(input())
    arr = list(map(int, input().split()))
    rear = 7
    front = -1
    m = 0
    while arr[rear % 8] != 0:
        front = (front + 1) % 8
        rear = (rear + 1) % 8
        if arr[front] - (m % 5 + 1) <= 0:
            arr[rear] = 0
        else:
            arr[rear] = arr[front] - (m % 5 + 1)
        m += 1

    print(f'#{T}', end = ' ')
    for i in range(1, 9):
        print(arr[(rear + i) % 8], end= ' ')
    print()