# import sys
# sys.setrecursionlimit(10**6)

def find(N):
    ans = []
    if N == 1:
        return '*'

    arr = find(N // 3)

    for i in range(N // 3):
        ans.append(arr[i] * 3)

    for i in range(N // 3):
        ans.append(arr[i] + ' ' * (N // 3) + arr[i])

    for i in range(N // 3):
        ans.append(arr[i] * 3)

    return ans


N = int(input())
for i in find(N):
    print(i)