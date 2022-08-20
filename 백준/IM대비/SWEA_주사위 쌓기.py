
N = int(input())

# 위, 좌, 앞, 우, 뒤, 아래

lst = []

for i in range(N):
    up, left, forward, right, back, under = map(int, input().split())
    lst.append([(up, under), (left, right) , (forward, back)])

ans = []
for i in range(1, 7):
    total = 0
    for l in range(len(lst)):
        big = 0
        for x, y in lst[l]:
            if l == 0:
                if x != i and y != i:
                    if big < max(x, y):
                        big = max(x, y)
            else:
                if x == i or y == i:
                    if x == i:
                        i = y
                    else:
                        i = x
                else:
                    if big < max(x, y):
                        big = max(x, y)
        total += big

    ans.append(total)
print(max(ans))

