import sys
input = sys.stdin.readline
N = int(input())


arr_x = []
arr_y = []
for i in range(N):
    x, y = map(int, input().split())
    arr_x.append(x)
    arr_y.append(y)

arr_x.sort()
arr_y.sort()

total = 0
for i in range(N):
    total += abs(arr_x[i] - arr_x[N // 2])
    total += abs(arr_y[i] - arr_y[N // 2])

print(total)


