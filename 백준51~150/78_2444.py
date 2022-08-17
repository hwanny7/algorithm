

n = int(input())
k = 1
for i in range(n):
    s = '*' * k
    print(s.center(2*n-1,' ').rstrip())
    k += 2
k -= 2
for i in range(n-1):
    k -= 2
    s = '*' * k
    print(s.center(2 * n - 1, ' ').rstrip())