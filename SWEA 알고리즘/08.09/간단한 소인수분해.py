
for t in range(1, int(input())+1):
    n = int(input())
    lst = [0] * 12
    s = 2
    while n != 1:
        if n % s == 0:
            n = n / s
            lst[s] += 1
        else:
            s += 1
    print(f'#{t}',lst[2], lst[3], lst[5], lst[7], lst[11])

