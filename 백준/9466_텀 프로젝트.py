import sys
sys.setrecursionlimit(111111)
input = sys.stdin.readline

def dfs(x, deep, turn):

    if visit[x]:        # 이미 방문을 했는데 이번 차례에 방문을 했는지, 아니면 저번 차례인지 확인해야함
        if visit[x] == turn:
            return deep - deep_lst[x]
        return 0

    visit[x] = turn
    deep_lst[x] = deep

    return dfs(arr[x], deep + 1, turn)





for t in range(int(input())):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    ans = 0
    visit = [0] * (N + 1)
    deep_lst = [0] * (N + 1)

    for i in range(1, N + 1):
        if not visit[i]:      # 방문한 적이 없다면
            ans += dfs(i, 1, i)  # i번째 학생 입장

    print(N - ans)

