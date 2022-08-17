

n = int(input())

sub = 1
for i in range(n):
    s = '*' * (2*n-sub)
    print(s.center(2*n-1,' ').rstrip())
    sub += 2
