
for tc in range(1, int(input()) + 1):
    P1 = [0] * 10
    P2 = [0] * 10
    card = list(map(int, input().split()))
    ans = 0
    for i in range(0, 12, 2):
        P1[card[i]] += 1
        for j in range(8):
            if P1[j] == 3:
                ans = 1
                break
            elif P1[j] and P1[j + 1] and P1[j + 2]:
                ans = 1
                break
        if ans:
            break

        P2[card[i + 1]] += 1
        for j in range(8):
            if P2[j] == 3:
                ans = 2
                break
            elif P2[j] and P2[j + 1] and P2[j + 2]:
                ans = 2
                break
        if ans:
            break

    print(f'#{tc}', ans)

