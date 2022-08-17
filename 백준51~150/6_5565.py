

total = int(input())
lst = []

for i in range(9):
    n = int(input())
    lst.append(n)

print(total-sum(lst))