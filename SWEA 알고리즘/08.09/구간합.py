for T in range(1, int(input())+1):
    l , n = map(int, input().split())
    nums = list(map(int, input().split()))
    lst = []
    for i in range(n, l+1):
        total = 0
        for j in range(i-n, i):
            total += nums[j]
        lst.append(total)
    max = lst[0]
    min = lst[0]
    for k in range(1, len(lst)):
        if lst[k] > max:
            max = lst[k]
        elif lst[k] < min:
            min = lst[k]
    print(f'#{T}', max - min)