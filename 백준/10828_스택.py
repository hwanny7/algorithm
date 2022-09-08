import sys
input = sys.stdin.readline

def push(x):
    global stack
    stack += 1
    nums[stack] = x
    return
def pop():
    global stack
    if stack == -1:
        return -1
    else:
        stack -= 1
        return nums[stack + 1]
def size():
    global stack
    return stack + 1
def empty():
    global stack
    if stack == -1:
        return 1
    else:
        return 0
def top():
    global stack
    if stack == -1:
        return -1
    else:
        return nums[stack]

N = int(input())
stack = -1
nums = [0] * 10001
for i in range(N):
    n = input().rstrip()
    if n == 'top':
        print(top())
    elif n == 'size':
        print(size())
    elif n == 'empty':
        print(empty())
    elif n == 'pop':
        print(pop())
    else:
        n, x = n.split()
        push(int(x))
