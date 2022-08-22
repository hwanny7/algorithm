

arr = [list(map(int, input().split())) for _ in range(5)]
nums = [list(map(int, input().split())) for _ in range(5)]

ans = 0
count = 0
ans_lst = []
for num in nums:
    for n in num:
        count += 1
        for c in range(5):
            for r in range(5):
                if arr[c][r] == n:
                    arr[c][r] = 0
        ans = 0
        if 5 <= count:
            cross1 = 0      #대각선
            cross2 = 0
            for i in range(5):      # 대각선 구하기
                if arr[i][i] == 0:
                    cross1 += 1
                if arr[i][4-i] == 0:
                    cross2 += 1
                temp_r = 0
                temp_c = 0
                for j in range(5):
                    if arr[i][j] == 0:
                        temp_r += 1
                    if arr[j][i] == 0:
                        temp_c += 1
                if temp_r == 5:
                    ans += 1
                if temp_c == 5:
                    ans += 1
            if cross1 == 5:
                ans += 1
            if cross2 == 5:
                ans += 1
        if 3 <= ans:
            ans_lst.append(count)

print(min(ans_lst))
