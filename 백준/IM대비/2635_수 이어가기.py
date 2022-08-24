n = int(input())
a = n // 2
if a == 0:
    a = 1

cnt = 0
ans = []

while a <= n:
    lst = [n, a]
    total = 1
    while lst[-1] > -1:
        lst.append(lst[-2] - lst[-1])
        total += 1
    a += 1
    if cnt < total:
        cnt = total
        ans = lst[:-1]

print(cnt)
print(*ans)

