
x= int(input())
y = int(input())

lst = []
for i in range(x, y+1):
    if (i**0.5) % 1 == 0.0:
        lst.append(i)

if len(lst) == 0:
    print(-1)
else:
    print(sum(lst), min(lst))

