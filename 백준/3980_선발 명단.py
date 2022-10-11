
def find(K = 0, total = 0, used = 0):
    global ans
    if K == 11:
        ans = max(ans, total)
        return

    for i in range(11):
        if ground[K][i] == 0:
            continue
        if used & (1 << i):
            continue
        find(K + 1, total + ground[K][i], used | (1 << i))

for t in range(int(input())):
    ground = [list(map(int, input().split())) for _ in range(11)]
    ans = 0
    find()
    print(ans)
