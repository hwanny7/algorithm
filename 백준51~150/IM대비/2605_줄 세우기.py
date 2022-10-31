n = int(input())

nums = list(map(int, input().split()))

lst = [0] * n

for i in range(1, n + 1):
    lst[i-1] = i

for i in range(1, n + 1):
    temp = nums[i-1]
    for j in range(i-2, temp-1, -1):
        lst[j + 1] = lst[j]
    lst[temp] = i

for i in range(len(lst) - 1, -1, -1):
    print(lst[i], end = ' ')
