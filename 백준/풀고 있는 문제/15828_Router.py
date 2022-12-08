import sys
input = sys.stdin.readline

N = int(input())
N += 1
store = [0] * N
front = rear = 0

while True:
    num = int(input())
    if num == -1: break
    elif num and (rear + 1) % N != front % N:
        rear += 1
        store[rear % N] = num
    elif num == 0:
        front += 1

if front == rear:
    print('empty')
else:
    for i in range(front + 1, rear + 1):
        print(store[i % N], end=' ')
