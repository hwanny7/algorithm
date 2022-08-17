import sys; sys.stdin = open('의석이의 세로로 말해요.txt')

for t in range(1, int(input())+1):
    arr = [list(input()) for _ in range(5)]

    long = 0
    for i in arr:
        total = 0
        for j in i:
            total += 1
        if long < total:
            long = total

    sentence = ''
    for c in range(long):
        for r in range(5):
            try:
                sentence += arr[r][c]
            except:
                continue
    print(f'#{t}', sentence)
