
n = int(input())

num = int(input())
total = 0
for i in range(n):
    total += num % 10
    num //= 10
print(total)
