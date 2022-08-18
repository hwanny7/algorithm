

n = int(input())

arr = [1, 2]

for i in range(n-2):
    for j in range(len(arr)-1, len(arr)):
        arr.append(arr[j]+arr[j-1])
print(arr[n-1] % 10007)