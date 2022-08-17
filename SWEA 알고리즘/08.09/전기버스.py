for i in range(1, int(input())+1):
    k, n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    arr = [0] * (n+1)

    for lst in nums:
        arr[lst] += 1

    total = k
    count = 0
    for r in range(1, len(arr)-k):
        total -= 1
        if arr[r] == 1:
            Y = 0
            for j in range(r+1, r+1+total):
                Y += arr[j]
            if Y >=1:
                continue
            else:
                total = k
                count += 1

        elif arr[r] == 0 and total == 0:
            count = 0
            break
    else:
        if k > total:
            count+=1

    print(f'#{i}', count)