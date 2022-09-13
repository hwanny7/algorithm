def queen(C):
    global cnt
    if C == N + 1:
        cnt += 1
        print(arr)
        return
    for R in range(N):
        if not visited[R]:
            for i in range(N):
                if arr[i] and C - abs(R - i) == arr[i]:         # C - abs(R - i)가 마이너스가 되면 대각선 범위를 벗어나는 것이 된다.
                    break
            else:
                arr[R] = C
                visited[R] = 1
                queen(C + 1)
                arr[R] = 0
                visited[R] = 0

cnt = 0
N = int(input())
visited = [0] * N
arr = [0] * N
queen(1)            # 1부터 시작하는 이유는 if arr[i] 에서 값이 들어있는지 확인해야 하기 때문. 처음부터 0이 들어가면 0은 false값이기 때문에 값이 들어갔는데도 불구하고 if arr[i]에서 false가 됨
print(cnt)