dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def bfs(comb_list):
    global ans
    visited = [[0 for _ in range(N)] for _ in range(N)]
    queue = []
    for c, r in comb_list:
        visited[c][r] = 1
        queue.append((c, r))

    cnt = K

    while queue:
        c, r = queue.pop(0)

        for i in range(4):
            nc, nr = c + dc[i], r + dr[i]
            if 0 <= nc < N and 0 <= nr < N and U <= abs(arr[nc][nr] - arr[c][r]) <= D and not visited[nc][nr]:
                visited[nc][nr] = 1
                queue.append((nc, nr))
                cnt += 1

    ans = max(ans, cnt)




def combination(start, k, curr_comb):
    if k == K:
        bfs(curr_comb)
        return

    for i in range(start, N ** 2):
        num = arr[i // N][i % N]
        combination(start + 1, k + 1, curr_comb + [[i // N , i % N]])

    return





N, K, U, D = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
combination(0, 0, [])



print(ans)