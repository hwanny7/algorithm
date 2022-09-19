def find():
    ans = []
    for i in range(N):
        for j in range(M - 1, -1, -1):
            if arr[i][j] == '1':
                for k in range(j + 1, j - 55, -7):
                    ans.append(dic[int(arr[i][k - 7:k], 2)])
                return ans


for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    dic = {13: 0, 25: 1, 19: 2, 61: 3, 35: 4, 49: 5, 47: 6, 59: 7, 55: 8, 11: 9}
    ans = find()

    two = 0
    one = 0
    for i in range(0, 8, 2):
        two += ans[i]
        one += ans[i + 1]

    if (two + one * 3) % 10 == 0:
        print(f'#{t}', sum(ans))
    else:
        print(f'#{t}', 0)