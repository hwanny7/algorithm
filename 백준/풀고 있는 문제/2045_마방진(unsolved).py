import sys
input = sys.stdin.readline
sys.setrecursionlimit(25000*3)

def verify():
    total = []
    cross_1 = 0
    cross_2 = 0
    for i in range(3):
        cross_1 += arr[i][i]
        cross_2 += arr[i][2 - i]
        c = 0
        r = 0
        for j in range(3):
            c += arr[i][j]
            r += arr[j][i]
        total.append(c)
        total.append(r)
    total.append(cross_1)
    total.append(cross_2)
    if len(set(total)) == 1:
        return 1

def track(K):
    if K == cnt:
        return verify()

    for i in range(1, 20001):
        arr[C[K][0]][C[K][1]] = i
        N = track(K + 1)
        if N == 1:
            return 1

arr = [list(map(int, input().split())) for _ in range(3)]

C = []
cnt = 0
for i in range(3):
    for j in range(3):
        if arr[i][j] == 0:
            C.append([i, j])
            cnt += 1

track(0)
for i in arr:
    print(*i)
