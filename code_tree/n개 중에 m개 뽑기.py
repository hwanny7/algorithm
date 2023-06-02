def combination(start, k, curr_comb):
    if k == K:
        print(*curr_comb)
        return

    for i in range(start, N):
        combination(i + 1, k + 1, curr_comb + [nums[i]])





N, K = map(int, input().split())
nums = [i for i in range(1, N + 1)]
combination(0, 0, [])