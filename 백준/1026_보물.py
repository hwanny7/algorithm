
N = int(input())

arr = list(map(int, input().split()))
arr1 = list(map(int, input().split()))


arr.sort()
arr1.sort(reverse = True)
total = 0
for i in range(N):
    total += arr[i] * arr1[i]


print(total)