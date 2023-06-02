def permutation(k, curr_per, used):
    if k == N:
        print(*curr_per)
        return

    for i in range(N):
        if used & (1 << i):
            continue
        permutation(k + 1, curr_per + [arr[i]], used | (1 << i))
        

    return




N = int(input())


arr = [i for i in range(N, 0, -1)]
permutation(0, [], 0)


