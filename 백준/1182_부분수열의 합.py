import sys
input = sys.stdin.readline

def combination(idx, sum = 0):
    global ans

    if idx == N:
        if sum == target:
            ans += 1
        return

    combination(idx + 1, sum + arr[idx])
    combination(idx + 1, sum)


N, target = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = 0
combination(0)
print(ans if target != 0 else ans - 1)
