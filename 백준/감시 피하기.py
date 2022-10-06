def select(start = 0, K = 0, lst = []):
    if K == 3:
        for tc, tr, sc, sr in between:
            for c, r in lst:
                if tc == sc:
                    if (tc, tr) < (c, r) < (sc, sr) or (sc, sr) < (c, r) < (tc, tr):
                        break
                else:
                    if (tr, tc) < (r, c) < (sr, sc) or (sr, sc) < (r, c) < (tr, tc):
                        break
            else:
                return 0

        return 1

    for i in range(start, len(X)):
        lst.append(X[i])
        check = select(i + 1, K + 1, lst)
        if check:
            return 1
        lst.pop()

N = int(input())

arr = [list(input().split()) for _ in range(N)]
S = []
T = []
X = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'S':
            S.append((i, j))
        elif arr[i][j] == 'T':
            T.append((i, j))
        else:
            X.append((i, j))

between = []
for tc, tr in T:
    for sc, sr in S:
        if tc == sc or tr == sr:
           between.append((tc, tr, sc, sr))

ans = select()

if ans:
    print('YES')
else:
    print('NO')
