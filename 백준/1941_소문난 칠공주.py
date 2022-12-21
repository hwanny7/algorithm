

from sys import stdin
input = stdin.readline
def check(include):
    here = [[0] * 5 for _ in range(5)]
    c, r = include
    queue = [[c, r]]
    here[c][r] = 1

    dc = [-1, 1, 0, 0]
    dr = [0, 0, -1, 1]

    cnt = 0

    while queue:
        c, r = queue.pop(0)
        cnt += 1
        for i in range(4):
            nc = dc[i] + c
            nr = dr[i] + r
            if 0 <= nc < 5 and 0 <= nr < 5 and visit[nc][nr] and not here[nc][nr]:
                queue.append([nc, nr])
                here[nc][nr] = 1

    return True if cnt == 7 else False

def dfs(i, deep, dic, include):
    global ans
    if dic['Y'] == 4:
        return

    if deep == 7:
        if check(include):
            ans += 1
        return

    for i in range(i, 25):
        c, r = load[i]
        visit[c][r] = 1
        dic[arr[c][r]] += 1

        dfs(i + 1, deep + 1, dic, [c, r])

        visit[c][r] = 0
        dic[arr[c][r]] -= 1



arr = [input() for _ in range(5)]
visit = [[0] * 5 for _ in range(5)]

load = []           #부분집합을 만들 좌표 생성
for i in range(5):
    for j in range(5):
        load.append((i, j))
ans = 0
dfs(0, 0, {'Y': 0, 'S': 0}, [])
print(ans)



# 다른 사람 코드
# import sys
#
# input = sys.stdin.readline
#
# dx = (-1, 1, 0, 0)
# dy = (0, 0, -1, 1)
#
# board = [list(input().rstrip()) for _ in range(5)]
#
# ans = 0
# check = set()
#
# def dp(arr, crew, Y):
#     global ans
#
#     print(arr)
#
#     if tuple(sorted(arr)) in check:
#         return
#
#     check.add(tuple(sorted(arr)))
#
#     if crew == 7:
#         ans += 1
#         return
#
#     next_pos = set()
#
#     for x, y in arr:
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if not (0 <= nx < 5 and 0 <= ny < 5):
#                 continue
#             if (nx, ny) in arr:
#                 continue
#             next_pos.add((nx, ny))
#
#     for nx, ny in next_pos:
#         if board[nx][ny] == 'S':
#             dp(arr | {(nx, ny)}, crew + 1, Y)
#         else:
#             if Y < 3:
#                 dp(arr | {(nx, ny)}, crew + 1, Y+1)
#
#
# for r in range(5):
#     for c in range(5):
#         if board[r][c] == 'S':
#             dp({(r, c)}, 1, 0)
