import sys
input = sys.stdin.readline

def push(x):
    global top
    top += 1
    stack[top] = x

def pop():
    global top
    top -= 1
    return stack[top + 1]

N = int(input())
size = [0] * 1000001

nums = list(map(int, input().split()))

for i in range(N):
    size[nums[i]] += 1

stack = [0] * (N + 1)
top = -1
push(nums[-1])
ans = [-1]

for i in range(N - 2, -1, -1):
    while top != -1:
        temp = pop()
        if size[nums[i]] < size[temp]:
            ans.append(temp)
            push(temp)
            push(nums[i])
            break
    if top == -1:
        ans.append(-1)
        push(nums[i])

print(*ans[::-1])







