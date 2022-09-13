nums = []
verify = []
for i in range(int(input())):
    n = input()
    if n in verify:
        continue
    verify.append(n)
    nums.append([n, len(n)])

nums.sort(key = lambda x: (x[1], x[0]))

for i, j in nums:
    print(i)