def reverse(arr):

    N= len(arr)
    for i in range(N // 2):
        if arr[i] == arr[N-i-1]:
            arr[i], arr[N-i-1] = arr[N-i-1], arr[i]
        else:
            return 0
            break

    else:
        return 1

for t in range(1, int(input())+1):
    word = list(map(str, input()))
    print(f'#{t}', reverse(word))