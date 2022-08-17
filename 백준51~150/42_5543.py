
lst = []
for i in range(5):
    n = int(input())
    lst.append(n)

l = []
for i in range(3):
    for j in range(3,5):
        l.append(lst[i]+lst[j]-50)
print(min(l))