arr = [7, 2, 5, 3, 4, 6]
N = len(arr)

for i in range(N-1): #1번부터 10번까지 있으면 1~9까지만
    minidx = i
    for j in range(i+1, N):
        if arr[minidx] > arr[j]:
            minidx = j
    arr[i], arr[minidx] = arr[minidx], arr[i]  # 최소값 인덱스를 다 찾은 뒤에 자리를 바꿔야함
print(arr)
