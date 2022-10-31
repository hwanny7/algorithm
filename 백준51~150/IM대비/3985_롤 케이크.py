
n = int(input())

stack = [0] * n

max = 0
who = 0

for i in range(1, int(input()) + 1):
    x, y = map(int, input().split())
    if max < y - x:
        max = y - x
        who = i
    for j in range(x - 1, y):
        if stack[j] == 0:
            stack[j] = i

first = [0, 0]
for i in range(1, n + 1):
    if first[0] < stack.count(i):
        first[0] = stack.count(i)
        first[1] = i

print(who)
print(first[1])