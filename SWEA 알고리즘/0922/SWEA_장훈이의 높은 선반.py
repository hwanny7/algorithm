

for t in range(1, int(input()) + 1):
    P, cm = map(int, input().split())
    arr = list(map(int, input().split()))

    ans = []
    temp = [0]
    for i in range(len(arr)):
        for j in range(len(temp)):
            m = temp[j] + arr[i]
            temp.append(m)
            if cm <= m:
                ans.append(m)

    print(f'#{t}', sorted(ans)[0] - cm)


