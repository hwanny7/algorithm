import sys

def Tree(x, idx, word):
    if len(word) - 1 < x - 1:
        return 1

    left = Tree(x * 2, idx, word)
    right = Tree(x * 2 + 1, idx, word)
    if left and right:
        return 1
    else:
        return 0




N, M = map(int, sys.stdin.readline().split())

words = []
for i in range(N):
    words.append(sys.stdin.readline().rstrip())

ans = 0
for i in range(M):
    word = sys.stdin.readline().rstrip()
    for j in range(N):
        if word[0] == words[j][0] and Tree(1, j, word):
            ans += 1
            break

print(ans)

# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())

# words = []
# for i in range(N):
#     word = input().rstrip()
#     words.append(word)

# ans = 0
# for i in range(M):
#     word = input().rstrip()
#     end = len(word)
#     for each in words:
#         each = each[:end]
#         if word == each:
#             ans += 1
#             break
# print(ans)