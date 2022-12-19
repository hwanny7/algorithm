
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []

for i in range(N):
    arr.append(int(input()))

arr.sort()
start = end = 0
ans = 0xffffffffff
# M 이상인 경우 Break
while end < N and start <= end:
    diff = abs(arr[start] - arr[end])
    if diff >= M:
        start += 1
        ans = min(ans, diff)
    else:
        end += 1


print(ans)