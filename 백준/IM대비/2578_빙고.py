

arr = [list(map(int, input().split())) for _ in range(5)]
nums = [list(map(int, input().split())) for _ in range(5)]

ans = []

count = 0
for num in nums:
    for n in num:
        count += 1
        for c in range(5):
            for r in range(5):
                if arr[c][r] == n:
                    arr[c][r] = 'X'
        for i in arr:
            print(*i)
            print(count)

            cross = 0
            cross2 = 0
            for i in range(5):
                if arr[i][i] == 'X':
                    cross += 1
                if arr[i][4-i] == 'X':
                    cross2 += 1
            r_final = 0
            c_final = 0
            for i in range(5):
                r = 0
                c = 0
                for j in range(5):
                    if arr[i][j] == 'X':
                        r += 1
                    if arr[j][i] == 'X':
                        c += 1
                if r == 5:
                    r_final = 5
                if c == 5:
                    c_final = 5
            # print(cross, cross2, r_final, c_final, count, n)

            if (cross == 5 or cross2 == 5) and r_final == 5 and c_final ==5:
                ans.append(count)



print(ans[0])




