
import sys

N, M = map(int, input().split()) # N 은 크기, M은 합의 횟수

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for c in range(N):
    for r in range(1, N):
        arr[c][r] = arr[c][r] + arr[c][r-1]

for i in range(M):
    total = 0
    x1, y1, x2, y2 = map(int, input().split())
    for c in range(x1 - 1, x2):
        if y1 - 1 != 0:
            total += arr[c][y2 - 1] - arr[c][y1 - 2]
        else:
            total += arr[c][y2 - 1]

    print(total)


