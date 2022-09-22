def perm(k, n, used):
    if k == n:
        m.append(order[:])

    for i in range(n):
        if used & (1 << i): continue
        order[k] = lst[i]
        perm(k + 1, n, used | (1 << i))

def cal(l):
    s = 0
    for i in range(N):
        s = arr[l[i]][l[i+1]]
    return s


for tc in range(1, 1+int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    lst = [i for i in range(2, N + 1)]
    order = [0] * (N - 1)
    m = []
    perm(0, N - 1, 0)
    max_s = 0
    print(m)
    # for i in lst_1:
    #     i = [1] + i + [1]
    #     k = cal(i)
    #     if k >= max_s:
    #         max_s = k
    print(max_s)