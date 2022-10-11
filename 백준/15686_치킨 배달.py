def find(k = 0, lst = [], start = 0):
    global ans

    if k == M:
        see = 0
        for c, r in house:
            total = 999999999999999
            for cc, rr in lst:
                temp = abs(c - cc) + abs(r - rr)
                if total > temp:
                    total = temp
            see += total
        if ans > see:
            ans = see
        return

    for i in range(start, len(chicken)):
        find(k + 1, lst + [chicken[i]], i + 1)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

chicken = []
house = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append([i, j])
        elif arr[i][j] == 2:
            chicken.append([i, j])

ans = 99999999999999999
find()
print(ans)