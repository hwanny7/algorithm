def combi(K, total):
    global min
    if K == N:
        total += arr[visit[K - 1] - 1][0]
        if min > total:
            min = total
        return
    elif total > min:
        return
    for j in range(2, N + 1):
        if not visited[j]:
            visit[K] = j
            visited[j] = 1
            combi(K + 1, total + arr[visit[K - 1] - 1][visit[K] - 1])
            visited[j] = 0


for t in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [1] + [0] * (N - 1) + [1]
    visited = [0] * (N + 1)
    min = 100000000000000000000
    combi(1, 0)
    print(f'#{t}', min)