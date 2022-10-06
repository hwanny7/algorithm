

C, R, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(C)]

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
air = []
Q = []
for i in range(C):
    for j in range(R):
        if arr[i][j] > 0:
            Q.append([i, j])
        elif arr[i][j] < 0:
            air.append([i, j])

while Q:
    dic = {}
    for l in range(len(Q)):
        c, r = Q.pop(0)
        num = arr[c][r] // 5
        cnt = 0
        for i in range(4):
            nc = c + dc[i]
            nr = r + dr[i]
            if 0 <= nc < C and 0 <= nr < R and arr[nc][nr] != -1 and num > 0:
                dic[(nc,nr)] = dic.get((nc, nr), arr[nc][nr]) + num
                cnt += 1
        dic[(c, r)] = dic.get((c, r), arr[c][r]) - num * cnt


    for key, value in dic.items():      # 에어컨 자리에 있으면 arr 에서 자리 옮기고 stack에 넣기
        c, r = key
        arr[c][r] = value



for i in arr:
    print(*i)