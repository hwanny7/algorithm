def V(x, y):
    if x == 1:
        return R - y
    if x == 3:
        return R + y
    if x == 2:
        return R + C + y
    if x == 4:
        return R * 2 + C * 2 - y

R, C = map(int, input().split())
store = int(input())
lst = []

for i in range(store):
    dir, dis = map(int, input().split())
    lst.append(V(dir, dis))

m_dir, m_dis = map(int, input().split())
first = V(m_dir, m_dis)

total = 0
size = R * 2 + C * 2
for i in lst:
    if i < first:
        total += min(size - first + i, first - i)
    else:
        total += min(first + (size - i), (i - first))

print(total)
