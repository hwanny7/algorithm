import sys; sys.stdin = open('사다리1.txt')

for t in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    r = 0
    c = 98

    for i in range(100):
        if arr[99][i] == 2:     #목표지점 r 값 찾기
            r = i
            break

    while c != 0:
        if r + 1 <= 99 and arr[c][r+1] == 1:      #오른쪽 확인
            arr[c][r] = 2     #지나온 길을 1이 아닌 다른 수로 변경
            r += 1
        elif 0 <= r - 1 and arr[c][r-1] == 1:       #왼쪽 확인
            arr[c][r] = 2
            r -= 1

        else:
            c -= 1

    print(f'#{T}', r)