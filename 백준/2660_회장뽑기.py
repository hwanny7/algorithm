N = int(input())
V = [[] for _ in range(N + 1)]

while True:
    fir, sec = map(int, input().split())
    if fir == -1:
        break
    V[fir].append(sec)
    V[sec].append(fir)

ans = []
for i in range(1, N + 1):
    visit = [0] * (N + 1)
    Q = [i]
    visit[i] = 1
    max = 0
    while Q:
        num = Q.pop(0)
        for i in V[num]:
            if not visit[i]:
                Q.append(i)
                visit[i] = visit[num] + 1
                max = visit[i] - 1
    ans.append(max)
small = min(ans)
print(small, ans.count(small))
for i in range(N):
    if ans[i] == small:
        print(i + 1, end=' ')