import sys
from collections import deque
input = sys.stdin.readline
def find(start = 0, l = 0):
    global ans
    global total
    if l == 3:
        visit = [[0] * M for _ in range(N)]
        dr = [0, 0, -1, 1]
        dc = [-1, 1, 0, 0]
        Q = deque()
        for virus in double:
            Q.append(virus)
        temp = 3
        while Q:
            c, r = Q.popleft()
            for i in range(4):
                C = c + dc[i]
                R = r + dr[i]
                if 0 <= C < N and 0 <= R < M:
                    if arr[C][R] == 0 and visit[C][R] == 0:
                        temp += 1
                        visit[C][R] = 1
                        Q.append([C, R])

        ans = max((N * M) - (total + temp), ans)
        return

    for i in range(start, len(zero)):
        c, r = zero[i]
        arr[c][r] = 1
        find(i + 1, l + 1)
        arr[c][r] = 0


N, M = map(int, input().split()) # 세로, 가로
arr = [list(map(int, input().split())) for _ in range(N)]
zero = deque()
double = deque()
total = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            zero.append([i, j])
        elif arr[i][j] == 2:
            total += 1
            double.append([i, j])
        else:
            total += 1

ans = 0
find()
print(ans)