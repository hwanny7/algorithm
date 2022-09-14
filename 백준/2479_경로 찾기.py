import sys
input = sys.stdin.readline
from collections import deque

def bfs(v, fir):         #최단경로로 작성해야함 bfs 사용
    visited[v] = 1
    queue = deque()
    queue.append([v, fir])
    while queue:
        v = queue.popleft()
        if v[0] + 1 == end:
            return v
        dr = [-1, 1]
        for i in range(1, N):
            for j in range(2):
                r = v[0] + dr[j] * i
                if 0 <= r < N and visited[r] == 0:
                    nums = abs(V[r] - V[v[0]])
                    if (V[r] != V[v[0]] and nums & (nums - 1) == 0) or nums == 1:
                        v.append(r + 1)
                        v[0] = r
                        queue.append(v)
                        visited[r] = 1



# 1번부터 시작함.
N, K = map(int, input().split())

V = [0] * (N)
visited = [0] * (N)
dr = [-1, 1]
for i in range(N):
    arr = list(map(int, input().rstrip()))
    for j in range(K):
        if arr[j]:
            V[i] += 2 ** (K - 1 - j)

start, end = map(int, input().split())

ans = bfs(start - 1, start)
if start == end:
    print(start)
elif ans:
    print(*ans[1::])
else:
    print(-1)