def hello(cnt , N):
    if K == cnt:
        print(' '.join(ans))
        return

    for i in range(1, N + 1):
        if visit[i - 1]:
            continue
        ans[cnt] = str(i)
        visit[i - 1] = 1
        hello(cnt + 1, N)
        visit[i - 1] = 0


N, K = map(int, input().split())
visit = [0] * N
ans = [0] * K
lst = [hello(0, N)]