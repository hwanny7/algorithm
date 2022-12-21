def find(N, total = 0):
    print('hi')
    global cnt, K
    if total == K:
        cnt += 1
        if cnt == K:
            print(cnt)
            exit(0)
        return

    for i in range(1, 4):
        if total + i <= K:
            find(N, total + i)

N, K = map(int, input().split())
cnt = 1

