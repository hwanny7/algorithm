# 1. 동쪽 2. 서쪽 3. 남쪽 4. 북쪽

N = int(input())
q = []
for i in range(6):
    d, l = map(int, input().split())
    q.append([d, l])

for i in range(6):
    if q[i][0] == q[(i + 2) % 6][0] and q[(i + 1) % 6][0] == q[( i + 3) % 6][0]:
        b = (q[i][1] + q[( i + 2) % 6][1]) * (q[(i + 1) % 6][1] + q[( i + 3) % 6][1])
        s = q[(i + 1) % 6][1] * q[( i + 2) % 6][1]
        print((b - s) * N)
        break