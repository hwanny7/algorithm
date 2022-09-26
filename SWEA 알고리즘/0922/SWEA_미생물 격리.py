for t in range(1, int(input()) + 1):
    N, T, K = map(int, input().split())
    queue = []
    for i in range(K):
        temp = list(map(int, input().split()))
        queue.append(temp)

    dc = [0, -1, 1, 0, 0]
    dr = [0, 0, 0, -1, 1]
    dic = {1:2, 2:1, 3:4, 4:3}

    for i in range(T):
        verify = {}
        for j in range(len(queue)):
            c, r, num, dir = queue.pop(0)
            C = c + dc[dir]
            R = r + dr[dir]
            if C == 0 or R == 0 or C == N - 1 or R == N - 1:
                num //= 2
                dir = dic[dir]

            if verify.get((C, R)):
                V, num1, dir2 = verify[(C, R)]
                if num < V:
                    verify[(C, R)] = (V, num + num1, dir2)
                else: verify[(C, R)] = (num, num + num1, dir)

            else:
                verify[(C, R)] = (num, num, dir)

        ans = 0
        for n, d in verify.items():
            x, y = n
            useless, num, dir = d
            ans += num
            queue.append([x, y, num, dir])


    print(f'#{t}', ans)









