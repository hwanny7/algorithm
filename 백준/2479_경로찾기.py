import sys
from collections import deque
input = sys.stdin.readline


def find(S, E):
    visit = 0
    Q = deque()
    Q.append([S,[S]])
    Q = [[S, [S]]]
    visit |= (1 << S)
    while Q:
        S, ans = Q.pop(0)
        if S == E:
            return ans
        for i in range(1, N + 1):
            if visit & (1 << i):
                continue
            n = int(arr[S], 2)^int(arr[i], 2)
            if n & (n - 1) == 0:
                trace = ans[:]
                trace.append(i)
                Q.append([i, trace])
                visit |= (1 << i)

N, K = map(int, input().split())
arr = [0]
for i in range(N):
    arr.append(input())
start, end = map(int, input().split())
ans = find(start, end)
if ans:
    for i in ans:
        print(i, end=' ')
else:
    print(-1)

import sys
from collections import deque
input = sys.stdin.readline


def find(S, E):
    visit = 0
    Q = deque()
    Q = [[S, [S + 1]]]
    visit |= (1 << S)
    while Q:
        S, ans = Q.pop(0)
        if S == E:
            return ans
        for i in range(N):
            if visit & (1 << i):
                continue
            n = int(arr[S], 2)^int(arr[i], 2)
            if n & (n - 1) == 0:
                trace = ans[:]
                trace.append(i + 1)
                Q.append([i, trace])
                visit |= (1 << i)

N, K = map(int, input().split())
arr = [input() for _ in range(N)]
start, end = map(int, input().split())
ans = find(start - 1, end - 1)
if ans:
    print(*ans)
else:
    print(-1)