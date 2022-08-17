
lst = []
for i in range(1, 9):
    n = int(input())
    lst.append([n, i])


for i in range(7):
    max = i
    for j in range(i+1, 8):
        if lst[max][0] < lst[j][0]:
            max = j
    lst[i], lst[max] = lst[max], lst[i]


lst2 = []
total = 0
for i in range(5):
    total += lst[i][0]
    lst2.append(lst[i][1])
print(total)
print(*sorted(lst2))
