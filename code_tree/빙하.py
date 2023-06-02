dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]


def break_ice(queue, visited, k):
    ice = []
    cnt = len(queue)
    while queue:
        c, r = queue.pop(0)

        for i in range(4):
            nc, nr = c + dc[i], r + dr[i]
            if 0 <= nc < N and 0 <= nr < M and not visited[nc][nr]:
                if arr[nc][nr] == 0: # 물일 경우
                    queue.append((nc, nr))
                else: # 빙하일 경우
                    ice.append((nc, nr))
                visited[nc][nr] = 1

    if ice:
        break_ice(ice, visited, k + 1)
    else:
        print(k, cnt)


def bfs():
    queue = [(0, 0)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    ice = []
    while queue:
        c, r = queue.pop(0)

        for i in range(4):
            nc, nr = c + dc[i], r + dr[i]
            if 0 <= nc < N and 0 <= nr < M and not visited[nc][nr]:
                if arr[nc][nr] == 0: # 물일 경우
                    queue.append((nc, nr))
                else: # 빙하일 경우
                    ice.append((nc, nr))
                visited[nc][nr] = 1

    break_ice(ice, visited, 1)




N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
bfs()