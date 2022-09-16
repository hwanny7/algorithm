N, M = map(int, input().split())

dic = {}
for i in range(N):
    name = input()
    dic[name] = dic.get(name, 0) + 1

total = 0
ans = []
for j in range(M):
    name = input()
    if name in dic:
        total += 1
        ans.append(name)

print(total)
for i in sorted(ans):
    print(i)