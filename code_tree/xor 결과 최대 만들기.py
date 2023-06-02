

def combination(start, k, total):
    global ans
    if k == M:
        ans = max(ans, total)
        return


    for i in range(start, N):
        combination(i + 1, k + 1, total^arr[i])





N, M = map(int, input().split())
arr = list(map(int , input().split()))
ans = 0
combination(0, 0, 0)
print(ans)