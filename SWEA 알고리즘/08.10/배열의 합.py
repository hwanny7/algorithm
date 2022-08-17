# N = int(input())    # 모든 행의 합
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# s= 0
# for i in range(N):
#     for j in range(N):
#         s+= arr[i][j]
# print(s)

# 각행의 합을 구하고 그 중 최대값 출력

s = 0
for i in range(N):
    for j in range(N):
        if i==j:
            s += arr[i][j]   # 대각선 구하는 법

s = 0

for i in range(N):           # 더 효율적으로 대각선 구하는 법
    s += arr[i][i]

s = 0                      #반대로 대각선
for i in range(N):
    s += arr[i][N-1-i]


# n 이 홀수인 경우에 양쪽 대각선을 구하면 가운데에 있는 하나를 빼야한다.

