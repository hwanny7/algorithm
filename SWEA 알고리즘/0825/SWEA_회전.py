

for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    front = -1
    rear = N - 1
    M = M % N
    nums = list(map(int, input().split()))

    for i in range(M):
        front = (front + 1) % N
        rear = (rear + 1) % N
        nums[rear] = nums[front]

    print(f'#{t}', nums[front + 1])