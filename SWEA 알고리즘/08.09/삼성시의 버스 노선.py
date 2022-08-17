T = int(input())
for t in range(1, T+1):
    N = int(input())

    case = []
    for n in range(N):
        lst = list(map(int, input().split()))
        case.append(lst)

    P = int(input())
    station = [0]*P   # station 개수
    for p in range(P):
        point = int(input())
        for a, b in case:
            if a <= point <= b:
                station[p] += 1

    print(f'#{t}', *station)









#첫째 테스트 케이스 개수
# 버스노선
# i번째 버스 노선은 a 이상 b 이하 정류장만 다님
# 버스 노선이 2개가 있는데
# 첫번째 버스 노선은 1이상 3이하 정류장만 다니고
# 두번째 버스 노선은 2이상 5이하 정류장만 다닌다