
lst = []
for i in range(5):
    n = int(input())
    lst.append(n)

print(sum(lst) // len(lst))
print(sorted(lst)[len(lst)// 2])