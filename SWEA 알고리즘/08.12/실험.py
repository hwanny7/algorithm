
dr = [0, 0, -1, 1, +1, +1, -1, -1]  # 상, 하, 좌, 우, 대각선
dc = [-1, 1, 0, 0, -1, +1, +1, -1]
lst = []
for i in range(N):
    for j in range(N):
        total = 0
        for k in range(8):
            if 0 <= i+ dc[k] < N and 0 <= j + dr[k] < N:
                total += arr[i + dc[k]][j + dr[k]]
        lst.append(total)

print(lst)