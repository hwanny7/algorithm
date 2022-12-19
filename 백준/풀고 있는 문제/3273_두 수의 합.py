N = int(input())
arr = list(map(int, input().split()))
target = int(input())
visit = [0] * 1000001
ans = 0


for i in range(N):
    visit[arr[i]] = i


for i in range(N):
    index = target - arr[i]
    if index <= 1000000 and visit[index] and i < visit[index]:
        ans += 1

print(ans)