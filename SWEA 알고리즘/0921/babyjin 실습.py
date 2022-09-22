
'''
5
123123
124467
333444
444456
123444
'''
#=============================== 카운트 배열
T = int(input())
for tc in range(1, T +1):
    card = int(input())
    c = [0] * 12        # 같은 코드로 run과 triple을 한 코드에서 검사하기 위해서 여분의 2칸을 더 생성

    i = 0
    while i < 6:
        c[card % 10] += 1
        card //= 10
        i += 1

    tri = 0
    run = 0
    i = 1
    while i < 10:
        if c[i] >= 3:
            c[i] -= 3
            tri += 1        #3개 있으면 triple로 쓴다.
            continue
        if c[i] >= 1 and c[i + 1] >= 1 and c[i + 2] >= 1:
            c[i] -= 1
            c[i + 1] -= 1
            c[i + 2] -= 1
            run += 1
            continue        #같은 자리에서 run이 또 시작될 수 있으니까 다음 칸으로 가지 말고 같은 자리에서 체크하기

        i += 1              #두가지 다 해당 없을 경우 pass

    if run + tri == 2:
        print(f'#{tc} Baby Gin')
    else:
        print(f'#{tc} Lose')


#=============================== 완전탐색법
# def f(i, k):
#
#     if i == k:
#         run  = 0
#         tri = 0
#         if card[0] == card[1] and card[1] == card[2]:
#             tri += 1
#         if card[0]+1 == card[1] and card[1] + 1 == card[2]:
#             run += 1
#         if card[3] == card[4] and card[4] == card[5]:
#             tri += 1
#         if card[3]+1 == card[4] and card[4] + 1 == card[5]:
#             run += 1
#         if tri + run == 2:      # 찾았으면 중단
#             return 1
#         else:
#             return 0
#
#     else:
#         for j in range(i, k):
#             card[i], card[j] = card[j], card[i]
#             if f(i+1, k):
#                 return 1
#             card[i], card[j] = card[j], card[i]
#         return 0
#
# T = int(input())
# for tc in range(1, T +1):
#     card = list(map(int, input()))
#     ans = f(0, 6)
#     if ans:
#         print(f'#{tc} Baby Gin')
#     else:
#         print(f'#{tc} Lose')