from collections import deque


def bfs():
    queue = deque()
    queue.append([N, 0])
    verify = [0] * 1000001
    while queue:
        Hi, cnt = queue.popleft()
        cnt += 1
        a, b, c, d = Hi * 2, Hi + 1, Hi - 1, Hi - 10
        for i in [a, b, c, d]:
            if i == target:
                print(f'#{t}', cnt)
                return
            if 0 <= i <= 1000000 and verify[i] == 0:
                queue.append([i, cnt])
                verify[i] = 1


for t in range(1, int(input()) + 1):
    N, target = map(int, input().split())
    bfs()