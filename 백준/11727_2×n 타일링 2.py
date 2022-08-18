
# 재귀로 하면 맥시멈 걸림
# def paper(n):
#     if memo[n] == 0:
#        return paper(n-1) + paper(n-2) * 2
#     else:
#         return memo[n]
#
#
# n = int(input())
#
# memo = [0] * (n + 1)
# memo[0] = 1
# memo[1] = 3
# print(paper(n - 1) % 10007)

n = int(input())
arr = [1, 3]

for i in range(n-2):
    for j in range(len(arr)-1,len(arr)):
        arr.append(arr[j] + arr[j-1] * 2)
print(arr[n-1] % 10007)