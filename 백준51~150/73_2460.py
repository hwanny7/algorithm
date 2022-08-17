

lst = []
total = 0
while True:
    x, y = map(int, input().split())
    if y == 0:
        total = total - x + y
        lst.append(total)
        break
    total = total - x + y
    lst.append(total)
print(max(lst))