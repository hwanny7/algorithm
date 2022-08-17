n = int(input())

count = 1
lst = [0, 1]
while count != n:
    total = 0
    for i in range(len(lst)-2, len(lst)):
        total += lst[i]
    lst.append(total)
    count += 1

print(lst[-1])

