def combination(lst, deep = 0, used = 0):
    global ans

    if deep == len(A):
        num = int(''.join(lst))
        if num < B:
            ans = max(ans, num)
        return


    for i in range(len(A)):
        if A[i] == '0' and deep == 0:
            continue
        if used & (1 << i):
            continue
        lst[deep] = A[i]
        # print(lst, used)
        combination(lst, deep + 1, used | (1 << i))

A, B = input().split()
B = int(B)
ans = -1
combination([0] * len(A))
print(ans)