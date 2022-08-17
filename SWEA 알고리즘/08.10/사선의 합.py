N = int(input())    # 모든 행의 합
arr = [list(map(int, input().split())) for _ in range(N)]

s = [0] * (2*N-1)    # 사선의 합을 담을 케이스
for i in range(N):
    for j in range(N):
        s[i+j] += arr[i][j]      #s[i+j] 대각선의 행과 열의 합은 동일하다

print(s)