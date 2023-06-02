dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def bfs():
    global ans
    visited = [[0 for _ in range(N)] for _ in range(N)]
    new_queue = []
    cnt = 0
    for C, R in queue:
        visited[C][R] = 1
        cnt += 1
        new_queue.append((C, R))
    while new_queue:
        c, r = new_queue.pop(0)

        for i in range(4):
            nc, nr = c + dc[i], r + dr[i]
            if 0 <= nc < N and 0 <= nr < N and arr[nc][nr] == 0 and not visited[nc][nr]:
                visited[nc][nr] = 1
                new_queue.append((nc, nr))
                cnt += 1

    ans = max(ans, cnt)



def combinations(start, list_length, length, current_combination):
    if length == 0:
        bfs()
        return

    for i in range(start, list_length):
        C, R = rock_list[i]
        arr[C][R] = 0
        combinations(i + 1, list_length,length - 1, current_combination + [rock_list[i]])
        arr[C][R] = 1


N, K, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
rock_list = []
ans = 0

for i in range(N):
    for j in range(N):
        if arr[i][j]:
            rock_list.append([i, j])

queue = []
for i in range(K):
    C, R = map(int, input().split())
    queue.append((C - 1, R - 1))

combinations(0, len(rock_list), M, [])
print(ans)

