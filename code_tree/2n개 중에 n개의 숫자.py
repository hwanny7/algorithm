def combination(start, k, curr_total):
    global ans


    if k == N:
        ans = min(ans, abs(total - curr_total * 2))
        return


    for i in range(start, N * 2):
        combination(i + 1, k + 1, curr_total + arr[i])




N = int(input())

arr = list(map(int, input().split()))

total = sum(arr)
ans = 0xffff
combination(0, 0, 0)
print(ans)