
lst = []
for i in range(int(input())):
    n = int(input())
    if n != 0:
        lst.append(n)
    else:
        lst.pop()
print(sum(lst))