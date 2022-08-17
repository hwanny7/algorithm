n = int(input())
lst = [''] * (2*n-1)
for i in range(1, n+1):
    for j in range(2*n-1 - (2*i-1), 2*n-1):
        lst[j] = '*'
    print(''.join(lst).center(2*n-1).rstrip())
