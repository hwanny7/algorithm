def push(x):
    global stack
    stack += 1
    temp[stack] = x
    ans.append('+')
    return

def pop():
    global stack
    stack -= 1
    ans.append('-')
    return temp[stack + 1]


N = int(input())

nums = []
for i in range(N):
    n = int(input())
    nums.append(n)

stack = -1
temp = [0] * N
ans = []
idx = 0
for i in range(1, N + 1):
    push(i)
    while stack != -1:
        if temp[stack] == nums[idx]:
            pop()
            idx += 1
        else:
            break

if stack == -1:
    for i in ans:
        print(i)
else:
    print('NO')

