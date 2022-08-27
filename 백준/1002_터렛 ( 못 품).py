# https://itstory1592.tistory.com/33
# 원의 방정식 이용해서 풀어야함
for t in range(int(input())):
    x, y, r, x1, y1, r1 = map(int, input().split())
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    lst = []
    for i in range(4):
        if 0 <= x + dr[i] * r and 0 <= y + dc[i] * r:
            lst.append([x + dr[i] * r, y + dc[i] * r])
        if 0 <= x1 + dr[i] * r1 and 0 <= y1 + dc[i] * r1:
            lst.append([x1 + dr[i] * r1, y1 + dc[i] * r1])

    print(lst)

