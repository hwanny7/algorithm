N = 10
arr = [[0]* N for _ in range(N)]

r = c = 5
arr[r][c] = '*'
# arr[r - 1][c + 0] = 1
# arr[r + 1][c + 0] = 2
# arr[r + 0][c -1] = 3
# arr[r + 0][c +1] = 4     # 한 좌표의 모든 방면에 수동으로 바꿀 때
# for line in arr:
#     print(*line)

# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
# # for i in range(4):     # 5의
# #     nr = r + dr[i]
# #     nc = c + dc[i]
# #     arr[nr][nc] = i + 1

dr = [-1, -1, 1, 1]
dc = [-1, 1, 1, -1]     #대각으로 갈 때

#
for i in range(4):  # 방향을 선택
    for j in range(1, N):
        nr, nc = r + dr[i] * j, c +dc[i]* j
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            break
        arr[nr][nc] = i + 1



