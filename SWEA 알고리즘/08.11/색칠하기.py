import sys; sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    arr = [[0]*10 for _ in range(10)]
    count = 0
    for i in range(int(input())):
        a, b, c, d, e = map(int, input().split())
        for j in range(a, c+1):
            for k in range(b, d+1):
                arr[j][k] += e

    for j in arr:
        print(j)
        count += 1
    print(f'#{t}', count)