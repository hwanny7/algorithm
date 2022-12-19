import sys
def input(): return sys.stdin.readline().strip()

def cal(lst, long):
    sum = 0

    for i in range(long - 1):
        for j in range(i + 1, long):
            sum += arr[lst[i]][lst[j]] + arr[lst[j]][lst[i]]

    return sum

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0xfffffff

for i in range(1, (1 << N) - 1):
    one = []
    two = []
    for j in range(N):
        if i & (1 << j):
            one.append(j)
        else:
            two.append(j)
    ans = min(ans, abs( cal(one, len(one)) - cal(two, len(two) )))
    if ans == 0:        # 0 이 나온 순간부터 다음에 나오는 수들은 무의미해진다.
        print(ans)
        exit(0)

print(ans)