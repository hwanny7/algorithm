

for t in range(1, int(input())+1):
    n = int(input())
    lst = [[1]]
    count = 1
    while count < n:
        ans = []
        for i in range(1, len(lst)):
            ans.append(lst[count-1][i] + lst[count-1][i-1])
        else:
            lst.append([1] + ans + [1])
            count += 1

    print(f'#{t}')
    for i in lst:
        for j in i:
            print(j, end=' ')
        print()


'''

def comb(n, r):
    if r == 0 or n == r:
        memo[n][r] = 1
        return 1
    if memo[n][r]:
        return memo[n][r]
    
    memo[n][r] = comb(n-1, r-1) + comb(n -1, r)
    return memo[n][r]
    
print(comb(10,5)


###############################

for i in range(N):
    for j in range(0, i + 1):
        if j == 0 or i == j:
            memo[i][j] = 1
        else:
            memo[i][j] = memo[i - 1][j - 1] + memo[i -1][j]



'''