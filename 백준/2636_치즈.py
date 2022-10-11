# import sys
# from collections import deque
# input = sys.stdin.readline
#
# def find(c, r):
#     global cnt
#     visit[c][r] = 0
#     Q = deque()
#     Q.append([c, r])
#     dr = [0, 0, -1, 1]
#     dc = [-1, 1, 0, 0]
#     one = 0
#     while Q:
#         c, r = Q.popleft()
#         cnt = 0
#         for i in range(4):
#             nc = c + dc[i]
#             nr = r + dr[i]
#             if 0 <= nc < N and 0 <= nr < M:
#                 if arr[nc][nr] == 0 and visit[nc][nr]:
#                     visit[nc][nr] = 0
#                     Q.append([nc, nr])
#                 elif arr[nc][nr]:
#                     boundary.append((nc, nr))
#                     arr[nc][nr] = 0
#                     visit[nc][nr] = 0
#                     one += 1
#     if one:
#         cnt += 1
#
#
# N, M = map(int, input().split()) #세로, 가로
# arr = [list(map(int, input().split())) for _ in range(N)]
# visit = [[1] * M for _ in range(N)]
# boundary = deque()
# cnt = 0
#
# def cheese():
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] == 0 and visit[i][j]:
#                 find(i, j)
#                 return
# for i in arr:
#     print(*i)
# print()
# cheese()
# for i in arr:
#     print(*i)

import sys
from collections import deque
input = sys.stdin.readline
import copy

def find(c, r):
    global cnt, ans
    visit[c][r] = 0
    Q = deque()
    Q.append([c, r])
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    boundary = deque()
    count = 0
    while Q:
        for l in range(len(Q)):
            c, r = Q.popleft()
            for i in range(4):
                nc = c + dc[i]
                nr = r + dr[i]
                if 0 <= nc < N and 0 <= nr < M:
                    if arr[nc][nr] == 0 and visit[nc][nr]:
                        visit[nc][nr] = False
                        Q.append([nc, nr])
                    elif arr[nc][nr] and visit[nc][nr]:
                        boundary.append([nc, nr])
                        visit[nc][nr] = 0
                        count += 1

        if not Q and boundary:
            Q = copy.deepcopy(boundary)
            ans = count
            boundary = deque()
            cnt += 1
            count = 0

def cheese():
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0 and visit[i][j]:
                find(i, j)
                return

N, M = map(int, input().split()) #세로, 가로
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[True] * M for _ in range(N)]
cnt = 0
ans = 0
cheese()
print(cnt, ans)

