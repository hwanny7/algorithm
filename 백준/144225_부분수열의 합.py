def combination(num = 0, sum = 0, lst = []):
    if num == N:
        visit[sum] = 1
        print(lst)
        return

    combination(num + 1, sum, lst)
    combination(num + 1, sum + arr[num], lst + [arr[num]])


N = int(input())
arr = list(map(int, input().split()))
total = sum(arr)
visit = [0] * (total + 2)
combination()

print(visit.index(0))


print('===============')
## 부분집합을 구하는 방식이지만 비트 연산이 훨씬 느림

N = int(input())
arr = list(map(int, input().split()))
visit = [0] * (100000*20)


for i in range(1, 1 << N):
    sum = 0
    comb = []
    for j in range(N):
        if i & (1 << j):
            sum += arr[j]
            comb.append(arr[j])
    print(comb)
    visit[sum - 1] = 1

print(visit.index(0) + 1)