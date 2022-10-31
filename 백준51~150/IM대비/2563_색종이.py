
arr = [[0] * 101 for _ in range(101)]
n = int(input())
check = [0] * (n + 1)

for i in range(1, n+1):
    x, y = map(int, input().split())

    for c in range(y, y+10):
        for r in range(x, x+10):
            if arr[c][r] == 0:
                arr[c][r] = i
                check[i] += 1

print(sum(check))
