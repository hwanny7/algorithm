def bfs(x, lst):
    global total, cnt
    visit[x] = False
    total += many[x - 1]
    cnt += 1

    for target in path[x]:
        if target in lst and visit[target]:
            bfs(target, lst)



N = int(input())
ans = 0xfffffffff
path = [[] for _ in range(N + 1)]
many = list(map(int, input().split()))
for i in range(1, N + 1):
    arr = list(map(int, input().split()))
    for j in range(1, arr[0] + 1):
        path[i].append(arr[j])

arr = list(range(1, N + 1))

for i in range(1, 1 << N):
    lst = []
    for j in range(N):
        if i & (1 << j):
            lst.append(arr[j])

    #cnt, total, visit 초기화
    cnt = 0
    total = 0
    visit = [True] * (N + 1)
    bfs(lst[0], lst)

    if cnt == len(lst):
        temp = total
        cnt = total = 0
        visit = [True] * (N + 1)
        less = list(set(arr) - set(lst))

        if less:
            bfs(less[0], less)

            if cnt == len(less):
                ans = min(ans, abs(temp - total))


if ans == 0xfffffffff:
    print(-1)
else:
    print(ans)






