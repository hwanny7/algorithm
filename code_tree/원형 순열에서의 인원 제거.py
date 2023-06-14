from collections import deque

N, K = map(int, input().split())

arr = deque([i for i in range(1, N + 1)])

ans = []
while arr:
    for i in range(K - 1):
        front = arr.popleft()
        arr.append(front)
    ans.append(arr.popleft())

print(*ans)