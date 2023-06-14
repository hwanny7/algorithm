

# )이 들어왔을 때 짝이 없는 경우
# 마지막에 Stack이 남아 있는 경우

stack = []
line = input()
for i in range(len(line)):

    if line[i] == ')' and stack and stack[-1] == '(':
        stack.pop()
        continue

    stack.append(line[i])

if stack:
    print('No')
else:
    print('Yes')