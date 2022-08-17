N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

s1 = 0
s2 = 0
for i in range(N):
    for j in range(N):
        if i > j:               #대각선 아래
            s1 += arr[i][j]
        elif i < j:             #대각선 위
            s2 += arr[i][j]

print(s1, s2)


s1 = 0
s2 = 0
for i in range(N):    #위의 대각선에만 접근하면서 그 반대방향도 같이
    for j in range(i+1, N):
        s2 += arr[i][j]
        s1 += arr[j][i]

print(s1, s2)
