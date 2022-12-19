def comb(lst, L, sum):
    global ans

    if L == 2:
        ans = max(ans, sum)
        return

    for i in range(1, L - 1):
        side = lst[i - 1] * lst[i + 1]  # 제거하는 구슬의 양 옆의 값 계산
        temp = lst.pop(i)
        comb(lst, L - 1, sum + side)
        lst.insert(i, temp)


N = int(input())
arr = list(map(int, input().split()))
ans = 0
comb(arr, N, 0)
print(ans)