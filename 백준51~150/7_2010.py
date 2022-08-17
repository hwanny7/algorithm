import sys


n = int(sys.stdin.readline().rstrip())
lst = []
for i in range(n):
    c = int(sys.stdin.readline().rstrip())
    lst.append(c)

for j in range(n-1):
    lst[j] -= 1
print(sum(lst))