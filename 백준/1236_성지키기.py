
N, M = map(int, input().split()) # 세로 N, 가로 M

arr = [list(input()) for _ in range(N)]

r = 0
c = 0
for i in range(N):
    count = 0
    for j in range(M):
        if arr[i][j] == 'X':
            count += 1
            break
    if count == 0:
        r += 1

for i in range(M):
    count = 0
    for j in range(N):
        if arr[j][i] == 'X':
            count += 1
            break
    if count == 0:
        c += 1

if r > c:
    print(r)
else:
    print(c)