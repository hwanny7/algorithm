# def Tree(position, div, level = 0):
#     global high
#     if level == high:
#         return
#     div = div // 2
#     Tree(position - div, div, level + 1)
#     Tree(position + div, div, level + 1)
#     ans[level].append(arr[position])

def Tree(level):
    global index
    if level == 0:
        index += 1
        ans[level].append(arr[index])
    else:
        Tree(level - 1)
        index += 1
        ans[level].append(arr[index])
        Tree(level - 1)


high = int(input())
arr = list(map(int, input().split()))
ans = [[] for _ in range(high)]
index = -1
Tree(high - 1)

for i in ans[::-1]:
    print(*i)