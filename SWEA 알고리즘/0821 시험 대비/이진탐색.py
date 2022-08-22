

arr = [1, 2, 3, 4, 5, 6, 7, 8]
end = len(arr) - 1
start = 0
key = 2
while start <= end:
    middle = (start + end) // 2
    if arr[middle] == key:
        print("찾았습니다", middle)
        break
    elif arr[middle] > key:
        end = middle - 1
    else:
        start = middle + 1

print(1 // 2)