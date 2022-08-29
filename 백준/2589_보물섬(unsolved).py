import sys
input = sys.stdin.readline
from collections import deque

#각각의 좌표에서 최장거리를 산정해서 그 중에서 max를 찾아야함.

def bps(x, y):
    visited = [[-1] * R for _ in range(C)]      # visited 초기화
    visited[x][y] = 0
    global max      #해당 좌표에서 최장거리 저장할 변수
    queue = deque()
    queue.append([x, y])        #queue에 넣어주고
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    while queue:
        c, r = queue.popleft()
        for i in range(4):
            nc = c + dc[i]
            nr = r + dr[i]
            if 0 <= nc < C and 0 <= nr < R and visited[nc][nr] == -1 and arr[nc][nr] == 'L':        #주변 땅으로 계속 이동
                visited[nc][nr] = visited[c][r] + 1
                queue.append([nc, nr])
                if max < visited[nc][nr]:       # 이번에 방문하는 곳이 기존의 최장거리보다 더 멀은지 확인하고 max값 바꿔주기
                    max = visited[nc][nr]


C, R = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(C)]

max = 0
for i in range(C):
    for j in range(R):
        if arr[i][j] == 'L':        # 배열 순회하면서 L 만나면 bps 함수에 넣기
            bps(i, j)

print(max)
