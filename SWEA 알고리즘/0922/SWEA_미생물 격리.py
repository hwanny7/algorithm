for t in range(1, int(input()) + 1):

    N, T, K = map(int, input().split())
    queue = []
    arr = [[[] * N for _ in range(N)] for _ in range(N)]
    for i in range(K):
        temp = list(map(int, input().split()))
        queue.append(temp)

    dc = [0, -1, 1, 0, 0]
    dr = [0, 0, 0, -1, 1]
    dic = {1:2, 2:1, 3:4, 4:3}

    for i in range(T):
        l = len(queue)
        home = set()
        for j in range(l):
            c, r, num, dir = queue.pop(0)
            C = c + dc[dir]
            R = r + dr[dir]
            if not 0 <= C < N or not 0 <= R < N:
                dir = dic[dir]
                C = C + dc[dir] * 2
                R = R + dr[dir] * 2

            if C == 0 or R == 0 or C == N - 1 or R == N - 1:
                num //= 2

            arr[C][R].append([num, dir])
            home.add((C, R))

        for m in arr:
            print(m)
        print()

        ans = 0
        for i, j in home:
            l = len(arr[i][j])
            if l == 1:
                num, dir = arr[i][j][0]
                queue.append([i, j, num, dir])
                ans += num
                arr[i][j] = []

            else:
                num = 0
                idx = 0
                for k in range(l):
                    num += arr[i][j][k][0]
                    if arr[i][j][idx][0] < arr[i][j][k][0]:
                        idx = k
                queue.append([i, j, num, arr[i][j][idx][1]])
                ans += num
                arr[i][j] = []

    print(f'#{t}', ans)









