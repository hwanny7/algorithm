'''
5
2
-2 0 1
1 3 2
2
-1 -1 1
1 0 2
10
3 5 4
2 6 8
7 4 10
6 6 11
3 3 3
5 2 8
0 5 10
4 7 9
6 2 5
1 1 10
5
-1 -2 1
4 -2 1
7 9 2
10 10 3
0 3 1
8
1 1 8
-3 1 8
-4 0 4
3 3 6
-1 1 6
-4 4 7
-3 5 4
-1 -2 4
'''


def dfs(C, R, count, k):
    visited[C][R][k] = 1
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    queue = [[C, R]]
    while queue:
        c, r = queue.pop(0)
        max = 0
        for i in range(4):
            nc = c + dc[i]
            nr = r + dr[i]
            if 0 <= nc < 31 and 0 <= nr < 31 and visited[nc][nr][k] == 0 and arr[nc][nr] == 0:
                queue.append([nc, nr])
                visited[nc][nr][k] = visited[c][r][k] + 1
                max = visited[nc][nr][k]
        if max == count + 1:
            return

for t in range(1, int(input()) + 1):
    N = int(input())
    arr = [[0] * 31 for _ in range(31)]
    visited = [[[0] * N for _ in range(31)] for _ in range(31)]
    for i in range(N):
        x, y, count = map(int, input().split())
        n = dfs(15 + y, 15 + x, count, i)
        if n:
            print(f'{t}', n)

    for i in visited:
        print(*i)

