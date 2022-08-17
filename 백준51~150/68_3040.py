
lst = []
for i in range(9):
    n = int(input())
    lst.append(n)
l = len(lst)

for i in range(1<<l):
    lst2 = []
    for j in range(l):
        if i & (1<<j):
           lst2.append(lst[j])
    if len(lst2) == 7 and sum(lst2) == 100:
        print(*lst2, sep='\n')
        break