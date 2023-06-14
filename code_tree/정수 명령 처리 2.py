from collections import deque


queue = deque()

N = int(input())

for i in range(N):
    line = list(input().split())

    if line[0] == "push":
        queue.append(line[1])
    elif line[0] == "front":
        print(queue[0])
    elif line[0] == "size":
        print(len(queue))
    elif line[0] == "empty":
        print(0 if queue else 1)
    else:
        print(queue.popleft())
