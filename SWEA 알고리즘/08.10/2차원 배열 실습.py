N = int(input())      # 행과 열이 같을 경우
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        print(arr[i][j], end=' ')
    print()


N, M = int(input())     # 행과 열이 다를 경우
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        print(arr[i][j], end=' ')
    print()

#지그재그 순회

for i in range(N):    # (i % 2)는 홀수 짝수를 거르기 위한 장치
    for j in range(M) :
        print(arr[i][j + (M-1-2*j) * (i%2)])


