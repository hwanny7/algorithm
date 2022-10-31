# arr = list(input())
# stack = [[] for _ in range(len(arr))]
# top = -1
# status = 0
# for i in range(len(arr) - 1, -1, -1):
#     if status:
#         status = 0
#         continue
#     top += 1
#     cnt = 0
#     if arr[i] != '(':
#         stack[top] = arr[i]
#         continue
#     while True:
#         top -= 1
#         if stack[top] == ')':
#             stack[top] = cnt * int(arr[i - 1])
#             status = 1
#             break
#         elif type(stack[top]) == int:
#             cnt += int(stack[top])
#         else:
#             cnt += 1
# ans = 0
# while top != -1:
#     if type(stack[top]) == int:
#         ans += stack[top]
#     else:
#         ans += 1
#     top -= 1
# print(ans)

arr = list(input())
arr = ['1'] + ['('] + arr + [')']
stack = [[] for _ in range(len(arr))]
top = -1
idx = len(arr) - 1

while idx > 0:
    top += 1
    if arr[idx] != '(':
        stack[top] = arr[idx]
        idx -= 1
        continue
    cnt = 0
    while True:
        top -= 1
        if stack[top] == ')':
            stack[top] = cnt * int(arr[idx - 1])
            idx -= 2
            break
        if type(stack[top]) == int:
            cnt += stack[top]
        else:
            cnt += 1
print(stack[top])
