import sys
input = sys.stdin.readline

N, M = map(int, input().split())    # N 세로, M 가로
c, r, dir = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 0, 1, 0] # 0, 1, 2, 3 (북 > 좌, 동> 상, 남 > 우, 서 > 하)
dc = [0, -1, 0, 1] # 좌, 상, 우, 하
ans = 0

for_r = [0, 0, -1, 1]
for_c = [-1, 1, 0, 0]

while True:
    if arr[c][r] == 0:       # 현재 위치한 곳 청소
        arr[c][r] = 5
        ans += 1
    elif arr[c][r] == 1:
        break

    for i in range(4):
        check_c = for_c[i] + c
        check_r = for_r[i] + r
        if not arr[check_c][check_r]:
            break
    else:   # 사방 탐색했을 때 갈 곳이 없다면
        if dir == 0:
            c += 1
        elif dir == 2:
            c -= 1
        elif dir == 3:
            r += 1
        else:
            r -= 1
        continue

    nc = c + dc[dir]
    nr = r + dr[dir]
    if not arr[nc][nr]:
        c, r, = nc, nr
    dir = dir - 1 if dir else 3

print(ans)