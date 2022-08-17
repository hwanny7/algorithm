N = int(input())

arr = list(map(int, input().split()))
for i in range(N-1, 0, -1): # 9개면 9-1 인 8부터 시작
    for j in range(i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)