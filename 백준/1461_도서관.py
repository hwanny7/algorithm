N, M = map(int, input().split())

temp = list(map(int, input().split()))

minus = []
plus = []
max = 0     # 절대값 가장 큰 것 찾기
for i in temp:
    if i < 0:
        minus.append(i)
    else:
        plus.append(i)
    if max < abs(i):
        max = abs(i)        # 음수 양수 나누기

minus.sort()
plus.sort(reverse = True)   # 정렬하기

total = 0

for m in range(0, len(minus), M):
    total += abs(minus[m] * 2)

for p in range(0, len(plus), M):
    total += plus[p] * 2

print(total - max)  #total에서 절대값 가장 큰 거 빼주기





