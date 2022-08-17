
x, y = map(int, input().split())
max = 0
for i in range(min(x, y), 0, -1):
    if x % i == 0 and y % i == 0:
        max = i
        break

print(max)
print((x // max) * (y // max) * max)