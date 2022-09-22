def f(i, k, s):
    global minV
    if i == k:
        if minV > s:
            minV = s
    elif s >= minV:                         #가지치기
        return
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            f(i+1, k, s + arr[i][p[i]])     #바로 바로 합산 / ~번 행의 열이 결정이 됐어
            p[i], p[j] = p[j], p[i]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    P = [0] * N     # p[i] i행에서 선택한 열 번호
    minV = N*10
    f(0, N, 0)
    print(minV)