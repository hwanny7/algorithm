ans = 0


def find(i, k):
    global ans
    if i == k:
        total = 0
        for i in range(k - 1):
            total += abs(newArr[i] - newArr[i + 1])
        ans = max(ans, total)
        return

    for j in range(N):
        if not visit[j]:
            visit[j] = 1
            newArr[i] = arr[j]
            find(i + 1, k)
            visit[j] = 0


N = int(input())
arr = list(map(int, input().split()))
visit = [0] * N
newArr = [0] * N

find(0, N)
print(ans)
