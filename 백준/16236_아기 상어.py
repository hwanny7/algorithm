
# 0 빈칸, 9 아기 상어의 위치, 그 외 물고기의 크기
# 가장 처음의 아기 상어의 크기는 2
# 자신보다 큰 물고기 칸은 지나갈 수 없음. 같은 크기는 지나갈수만 있음.
# 먹을 수 있는 물고기가 1마리면, 그 물고기를 먹으러 간다
# 여러 마리일 경우 거리가 가장 가까운 물고기
# 거리는 그 칸으로 이동할 때, 지나야하는 칸의 최솟값
# 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리면 가장 왼쪽에 있는 물고기
# 아기 상어는 자신의 크기와 같은 크기의 물고기를 먹을 때마다 1씩 증가


# for 문을 통한 bfs
from collections import deque
import sys
input = sys.stdin.readline

def big():
    global cnt, size
    cnt += 1

    if cnt == size:
        size += 1
        cnt = 0




def bfs(c, r):
    global size, ans
    dis = [[0] * N for _ in range(N)]
    dis[c][r] = 1
    queue = deque()
    queue.append((c, r))
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]

    while queue:
        temp = []
        for _ in range(len(queue)):
            c, r = queue.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < N and dis[nc][nr] == 0:
                    if not arr[nc][nr] or arr[nc][nr] == size: # 빈칸이거나 같은 크기의 경우
                        queue.append((nc, nr))
                    elif arr[nc][nr] < size:
                        temp.append((nc, nr))

                    dis[nc][nr] = dis[c][r] + 1

        if temp:
            temp.sort(key = lambda x: (-x[0], -x[1]))
            c, r = sorted(temp, key = lambda x: (x[0], x[1]))[0]
            ans += dis[c][r] - 1
            arr[c][r] = 0
            big()       # 사이즈 조절
            bfs(c, r)
            return



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
size = 2
cnt = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            arr[i][j] = 0
            bfs(i, j)
            print(ans)
            exit(0)