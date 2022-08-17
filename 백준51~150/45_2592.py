
dic = {}
lst = []
for i in range(10):
    n = int(input())
    lst.append(n)
    if n not in dic:
        dic[n] = 1
    else:
        dic[n] += 1

max = 0
key = 0
for i, j in dic.items():
    if max < j:
        max = j
        key = i
print(int(sum(lst) / len(lst)))
print(key)