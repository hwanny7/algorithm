

N, M = map(int, input().split())

dic = {}
for i in range(N):
    temp = input()
    dic[temp] = 0

for i in range(M):
    temp = input()
    if temp in dic:
        dic[temp] += 1

total = 0

for i in dic.values():
    total += i
print(total)