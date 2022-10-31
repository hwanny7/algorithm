import sys
input = sys.stdin.readline
N, total = map(int, input().split())
arr = list(map(int, input().split()))
V = arr[:]
for i in range(1, N):
    arr[i] += arr[i - 1]

start = 0
end = 0
ans = 0xffffffffffffffff
while start <= end:
    if start != end and arr[end] - arr[start] + arr[start] >= total:
        ans = min(ans, end - start + 1)
        start += 1
    elif end + 1 < N:
        end += 1
    else:
        start += 1

if ans == 0xffffffffffffffff:
    print(0)
else:
    print(ans)