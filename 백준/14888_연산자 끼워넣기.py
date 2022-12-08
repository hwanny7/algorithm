



def find(deep, total):
    global ans_b
    global ans_s
    if deep == N:
        if total > ans_b:
            ans_b = total
        if total < ans_s:
            ans_s = total


    for i in range(long):
        if oper[i]:
            oper[i] -= 1
            if i == 0:
                find(deep + 1, total + nums[deep])
            elif i == 1:
                find(deep + 1, total - nums[deep])
            elif i == 2:
                find(deep + 1, total * nums[deep])
            elif i == 3:
                find(deep + 1, total // nums[deep] if total >= 0 else (abs(total) // nums[deep]) * - 1)
            oper[i] += 1




N = int(input())

nums = list(map(int, input().split()))
oper = list(map(int, input().split()))
long = len(oper)
ans_b = -10000000000
ans_s = 0xffffffffff
find(1, nums[0])

print(ans_b)
print(ans_s)
