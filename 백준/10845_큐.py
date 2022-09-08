import sys
input = sys.stdin.readline

def push(x):
    global rear
    rear += 1
    nums[rear] = x
    return

def pop():
    global top
    if rear == top:
        return -1
    else:
        top += 1
        return nums[top]

def empty():
    if top == rear:
        return 1
    else:
        return 0
def front():
    if top == rear:
        return -1
    else:
        return nums[top + 1]
def back():
    if top == rear:
        return -1
    else:
        return nums[rear]
def size():
        return (rear + 1) - (top + 1)



top = -1
rear = -1
nums = [0] * 10001
for i in range(int(input())):
    n = input().rstrip()
    if n == 'front':
        print(front())
    elif n == 'back':
        print(back())
    elif n == 'size':
        print(size())
    elif n == 'empty':
        print(empty())
    elif n == 'pop':
        print(pop())
    else:
        n, x = n.split()
        push(int(x))
