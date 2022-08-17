def B(x, y):
    N = len(x) #전체 텍스트
    M = len(y) # 패턴 길이

    i = 0  # t의 인덱스
    j = 0  # p의 인덱스
    count = 0

    while j < M and i < N:
        if x[i] != y[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
        if j == M:
            count += 1
            j = 0

    return N - (count * M) + count

for t in range(1, int(input())+1):
    x, y = input().split()
    print(f'#{t}', B(x, y))