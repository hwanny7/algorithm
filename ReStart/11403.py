




# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# for k in range(N):
#     for i in range(N):
#         for j in range(N):
#             if arr[i][k] and arr[k][j]:
#                 arr[i][j] = 1
#
# for i in range(N):
#     print(*arr[i])

def bfs(floor):
    queue = [floor]
    visit = [False] * N
    while queue:
        current_floor = queue.pop(0)
        for i in range(N):
            if arr[current_floor][i] and not visit[i]:
                visit[i] = True
                queue.append(i)
                arr[floor][i] = 1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    bfs(i)

for i in range(N):
    print(*arr[i])