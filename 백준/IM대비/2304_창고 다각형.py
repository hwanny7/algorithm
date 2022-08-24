

N = int(input())

lst = []

for i in range(N):
    x, y = map(int, input().split())
    lst.append((x, y))
lst.sort()

w = lst[0][0]
h = lst[0][1]

total = 0

for i in range(1, N):
    w1 = lst[i][0]
    h1 = lst[i][1]
    if i == N - 1:
        if h1 >= h:  # 높거나 같은 기둥을 만났을 때
            total += (w1 - w + 1) * h + h1 - h
            h = h1
            w = w1
        else:
            total += (w1 - w + 1) * h1 + h - h1
            h = h1
            w = w1
    if h1 >= h:     # 높거나 같은 기둥을 만났을 때
        total += (w1 - w) * h
        h = h1
        w = w1
    else:           # 작은 경우
        for j in range(i + 1, N):
            if lst[j][1] > h1:
                break
        else:
            total += (w1 - w) * h1 + h - h1
            h = h1
            w = w1

print(total)

