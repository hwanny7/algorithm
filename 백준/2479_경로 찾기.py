import sys
input = sys.stdin.readline
from collections import deque

def bfs(v,lst):         #최단경로로 작성해야함 bfs 사용
    visited[v] = 1
    queue = deque()
    for i in range():
        arr[n - 1] arr[n + 1] 형태로 작성해서 범위 확인하자 깔끔하게

# 1번부터 시작함.
N, K = map(int, input().split())

V = [0] * (N)
visited = [0] * (N)
dr = [-1, 1]
for i in range(N):
    arr = list(map(int, input().rstrip()))
    for j in range(K):
        if arr[j]:
            V[i] += 2 ** (K -1 - j)

start, end = map(int, input().split())

ans = bfs(start - 1, [])
if ans:
    print(*ans)
else:
    print(-1)


