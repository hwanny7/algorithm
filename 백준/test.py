
N = int(input())

# 위, 좌, 앞, 우, 뒤, 아래

lst = []

for i in range(N):
    up, left, forward, right, back, under = map(int, input().split())
    lst.append([(up, under), (left, right) , (forward, back)])

i = 1
g_total = []
while i != 7:
    total = 0
    box = 0
    for l in lst:
        big = 0
        for x, y in l:
            if x == i:
                box = y
            elif y == i:
                box = x
            else:
                big = max(x, y)
        i = box
        total += big
    g_total.append(total)
    i += 1

print(g_total)