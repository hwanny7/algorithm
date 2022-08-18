def ninety(arr):

    new_arr = [[0] * N for _ in range(N)]
    new_arr2 = [[0] * N for _ in range(N)]
    new_arr3 = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
                new_arr[j][N-1-i] = str(arr[i][j])
                new_arr2[N-1-i][N-1-j] = str(arr[i][j])
                new_arr3[N-1-j][i] = str(arr[i][j])

    return new_arr, new_arr2, new_arr3




for t in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N) ]
    a, b, c = ninety(arr)

    print(f'#{t}')
    for i in range(N):
            print(''.join(a[i]), ''.join(b[i]), ''.join(c[i]))