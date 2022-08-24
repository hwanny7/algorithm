# 선형 큐
N = 3
q = [0] * N
front = -1
rear = -1

rear += 1       # enqueue
q[rear] = 10

rear += 1       # enqueue
q[rear] = 20

rear += 1       # enqueue
q[rear] = 30

front += 1      # dequeue (실제로 데이터를 지운 것은 아님)
print(q[front])

# 순환 큐
N = 3
q = [0] * N
front = 0
rear = 0

rear = (rear + 1) % N       # enqueue
q[rear] = 10

rear = (rear + 1) % N
q[rear] = 20

rear = (rear + 1) % N
q[rear] = 30

rear = (rear + 1) % N       #배열보다 더 많은 데이터를 넣어도 순환구조기 때문에 삽입은 되지만 다른 데이터를 덮어쓰게 된다.
q[rear] = 40

front = (front + 1) % N      # dequeue (실제로 데이터를 지운 것은 아님)
print(q[front])

front = (front + 1) % N
print(q[front])

front = (front + 1) % N
print(q[front])


