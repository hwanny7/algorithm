import sys
from heapq import heappush, heappop
input = sys.stdin.readline

V, E = map(int, input().split())
path = [[] for _ in range(V + 1)]
for i in range(E):
    S, E, W = map(int, input().split())
    path[S].append((E, W))
    path[E].append((S, W))

MST = [0] * (V + 1)
Q = []
for i in range(V):
    heappush(Q, [2147483648, i + 1])
Q[0][0] = 0

total = 0
while Q:
    value, idx = heappop(Q)
    if MST[idx]:
        continue
    MST[idx] = 1
    total += value
    for E, W in path[idx]:
        if MST[E] == 0:
            heappush(Q, [W, E])


print(total)

