

N, M = map(int, input().split()) # N = 가로, M = 세로

r = [0, N] # 세로 자르기
c = [0, M] # 가로 자르기

for i in range(int(input())):
    a, b = map(int, input().split())

    if a == 0:
        c.append(b)
    else:
        r.append(b)

r.sort()
c.sort()

max_r = 0
max_c = 0

for i in range(1, len(r)):
    if max_r < r[i] - r[i-1]:
        max_r = r[i] - r[i-1]

for j in range(1, len(c)):
    if max_c <  c[j] - c[j-1]:
        max_c = c[j] - c[j-1]
print(max_r * max_c)