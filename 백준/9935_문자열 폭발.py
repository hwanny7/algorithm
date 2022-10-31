import sys
input = sys.stdin.readline
arr = input().rstrip()
word = input().rstrip()
stack = [[] for _ in range(len(arr))]
num = [-1] * len(arr)
top = -1
idx = 0
for i in arr:
    top += 1
    if i == word[0]:
        num[top] = 0

    elif i == word[num[top - 1] + 1]:
        num[top] = num[top - 1] + 1

    else:
        num[top] = -1
    stack[top] = i

    if num[top] == len(word) - 1:
        top = top - len(word)

if top <= -1:
    print('FRULA')
else:
    print(''.join(stack[:top + 1]))