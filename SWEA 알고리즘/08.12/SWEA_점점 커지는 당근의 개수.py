for t in range(1, int(input())+1):
    n = int(input())
    nums = list(map(int, input().split()))

    dic = {}
    for j in range(1, n):
        if nums[j] - nums[j - 1] in dic:
            dic[nums[j] - nums[j - 1]] += 1
        else:
            dic[nums[j] - nums[j - 1]] = 1
    print(dic)

    value = 0
    for keys, values in dic.items():
        if values > 0 and value < values:
            value = values

    print(value)