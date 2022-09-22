


for tc in range(1, int(input()) + 1):
    con, car = map(int, input().split())
    kg = list(map(int, input().split()))
    t = list(map(int, input().split()))
    kg.sort()

    total = 0
    for i in t:
        for j in range(len(kg) -1, -1, -1):
            if kg[j] <= i:
                total += kg.pop(j)
                break

    print(f'#{tc}', total)