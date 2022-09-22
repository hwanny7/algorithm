




for tc in range(1, int(input()) + 1):
    N = int(input())
    route = []
    for i in range(N):
        S, E = map(int, input().split())
        route.append([S, E])

    route.sort(key = lambda x:x[1])

    idx = 0
    cnt = 1
    for i in range(1, N):
        if route[idx][1] <= route[i][0]:
            idx = i
            cnt += 1

    print(f'#{tc}', cnt)
