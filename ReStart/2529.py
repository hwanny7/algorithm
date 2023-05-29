def combination(k, used, time):

    if k == N + 1:
        result = ''.join(map(str, selected))
        print(result)
        if time:
            exit()
        nums.reverse()
        combination(0, 0, 1)

        return

    for i in range(10):
        if used & (1 << i):
            continue
        if k > 0:
            if inequality[k - 1] == '<' and not selected[k - 1] < nums[i]:
                continue
            elif inequality[k - 1] == '>' and not selected[k - 1] > nums[i]:
                continue
        selected[k] = nums[i]
        combination(k + 1, used | (1 << i), time)




N = int(input())
inequality = list(input().split(' '))
nums = [i for i in range(9, -1, -1)]
selected = [0] * (N + 1)
combination(0, 0, 0)