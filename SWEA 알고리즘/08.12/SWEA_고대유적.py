import sys; sys.stdin = open('고대유적.txt')

for t in range(1, int(input())+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) + [0] for _ in range(N)]
    arr.append([0] * (M+1))

    for i in arr:
        print(*i)

    grand_total = []
    for i in range(N+1):
        total = 0
        for j in range(M+1):
            if arr[i][j] == 1:
                total += 1
            else:
                grand_total.append(total)
                total = 0

    for c in range(M+1):
       for h in range(N+1):
           if arr[h][c] == 1:
               total += 1
           else:
               grand_total.append(total)
               total = 0

    max = 0
    for m in grand_total:
        if max < m:
            max = m
    print(f'#{t}', max)