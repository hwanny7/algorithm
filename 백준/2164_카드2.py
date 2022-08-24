
N = int(input())
lst = list(range(1, N + 1))
rear = N - 1
front = -1
while front != rear:
    front = (front + 2) % N
    rear = (rear + 1) % N
    lst[rear] = lst[front]
print(lst[rear - 1])