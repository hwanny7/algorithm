def solution(s):
#     stack = []

#     for i in s:
#         if i == ')' and stack and stack[-1] == '(':
#             stack.pop()
#         else:
#             stack.append(i)


#     return False if stack else True
    pair = 0
    for x in s:
        if pair < 0: break
        pair = pair + 1 if x == "(" else pair - 1 if x == ")" else pair
        print(x, pair)
    return pair == 0

print(solution('(((()))'))