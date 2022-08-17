
for t in range(1, int(input())+1):
    n = int(input())
    nums = [list(map(int, input().split())) for _ in range(n)]

    dr = [1, 1, -1, -1] #대각선
    dc = [-1, 1, 1, -1]

    grand_total = 0
    for c in range(n):
        for r in range(n):
            total = nums[c][r]
            for k in range(1, n+1):
                for v in range(4):
                    if 0 <= c + dc[v] * k < n and 0 <= r + dr[v] * k < n:
                        total += nums[c + dc[v] * k][r + dr[v] * k]
            if grand_total < total:
                grand_total = total
    print(f'#{t}', grand_total)
