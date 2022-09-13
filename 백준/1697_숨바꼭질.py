import sys
input = sys.stdin.readline
from collections import deque

def bfs(st):
    queue = deque()
    queue.append([st, 0])
    while queue:
        W, C = queue.popleft()
        if W == M:
            return C
        for i in [W, 1, -1]:
            if 0 <= W + i <= 100000 and visited[W + i] == 0:
                queue.append([W + i, C + 1])
                visited[W + i] = 1


N, M = map(int, input().split())
visited = [0] * 100001
print(bfs(N))