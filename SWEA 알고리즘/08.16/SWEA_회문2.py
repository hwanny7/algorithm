def length(M):
    for c in range(100):
        for r in range(100-M+1):
            for turn in range(M // 2):
                if arr[c][r+turn] != arr[c][r+M-1-turn]:
                    break
            else:
                return M
def height(M):
    for r in range(100):
        for c in range(100-M+1):
            for turn in range(M // 2):
                if arr[c+turn][r] != arr[c+M-1-turn][r]:
                    break
            else:
                return M



for i in range(10):
    T = int(input())
    arr = [list(input()) for _ in range(100)]
    i = 22
    while True:
        if length(i):
            print(f'#{T}', length(i))
            break
        elif height(i):
            print(f'#{T}', height(i))
            break
        i -= 1