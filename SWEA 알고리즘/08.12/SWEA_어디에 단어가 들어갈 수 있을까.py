import sys; sys.stdin = open('어디에.txt')

for t in range(1, int(input())+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)]
    arr.append([0] * (N+1))

    how_many = 0
    for i in range(N+1):
        long = 0
        long2 = 0
        for j in range(N+1):
            if arr[i][j] == 1:
                long += 1
            else:
                if long == K:
                    how_many += 1
                long = 0
            if arr[j][i] == 1:
                long2 += 1
            else:
                if long2 == K:
                    how_many += 1
                long2 = 0

    print(f'#{t}', how_many)
