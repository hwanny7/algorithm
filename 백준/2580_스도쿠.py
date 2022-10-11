import sys
input = sys.stdin.readline

def find(k = 0):
    if k == len(empty):
        for i in arr:
            print(*i)
        exit(0)

    c, r = empty[k]
    for i in range(1, 10):
        if R[c][i] and C[r][i] and real[c // 3][r // 3][i]:
            arr[c][r] = i
            R[c][i] = False
            C[r][i] = False
            real[c // 3][r // 3][i] = False
            find(k + 1)
            R[c][i] = True
            C[r][i] = True
            real[c // 3][r // 3][i] = True


arr = [list(map(int , input().split())) for _ in range(9)]
empty = []
R = []
C = []
for i in range(9):
    ten_rr = [True] * 10
    ten_cc = [True] * 10
    for j in range(9):
        if not arr[i][j]:
            empty.append([i, j])
        ten_rr[arr[i][j]] = False
        ten_cc[arr[j][i]] = False
    R.append(ten_rr)
    C.append(ten_cc)

real = []
for i in range(0, 9, 3):
    three = []
    for j in range(0, 9, 3):
        ten_33 = [True] * 10
        for c in range(i, i + 3):
            for r in range(j, j + 3):
                ten_33[arr[c][r]] = False
        three.append(ten_33)
    real.append(three)
find()