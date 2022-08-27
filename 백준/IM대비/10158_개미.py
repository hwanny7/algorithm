import sys

W, H = map(int, sys.stdin.readline().split())
r, c = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())



for i in range(t):
r이 w 보다 커지면 좌우 반전, c가 h보다 커지면 상,하 반전
c가 0보다 작아지면 상,하 반전, r이 0보다 작아지면 좌우 반전


dr = 1
dc = 1

for i in range(t):
    nr = r + dr
    nc = c + dc
    if nr < 0 or W < nr:    # r이 0보다 작을 때, 좌우 반전
        dr *= -1
        r += dr
    else:
        r += dr
    if nc < 0 or H < nc:
        dc *= -1
        c += dc
    else:
        c += dc

print(r, c)
