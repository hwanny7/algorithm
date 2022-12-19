def find(deep = 0, ans = []):
    if deep == M:
        print(*ans)
        return

    for i in range(N):
        find(deep + 1 , ans + [arr[i]])




N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
find()
