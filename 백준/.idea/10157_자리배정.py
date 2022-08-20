

R, C = map(int, input().split()) # C는 가로, R은 세로
num = int(input())

dr = [1, 0, -1, 0] #우, 하, 좌, 상
dc = [0, 1, 0, -1]

arr = [[0] * C for _ in range(R)]

r = -1
c = 0
x = 0
box = []
for i in range(1, R*C+1):
        if 0 <= r+dr[x % 4] < C and 0 <= c+dc[x % 4] < R and arr[c+dc[x % 4]][r+dr[x % 4]] == 0:
            arr[c+dc[x % 4]][r+dr[x % 4]] = i
            r = r + dr[x % 4]
            c = c + dc[x % 4]
        else:
            x += 1
            arr[c + dc[x % 4]][r + dr[x % 4]] = i
            r = r + dr[x % 4]
            c = c + dc[x % 4]
        if i == num:
            box = [c+1, r+1]

if len(box) == 0:
    print(0)
else:
    print(*box)