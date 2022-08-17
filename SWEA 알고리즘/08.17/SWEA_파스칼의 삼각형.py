

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
