
total = 0
for t in range(int(input())):
    x, y = map(int, input().split())
    total += y % x
print(total)