
total = 0
lst = []
for i in range(4):
    x, y = map(int, input().split())
    total = total - x + y
    lst.append(total)
print(max(lst))
