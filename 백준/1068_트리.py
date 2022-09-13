import sys
input = sys.stdin.readline

def Tree(st):
    global cnt
    if not V[st]:
        cnt += 1
        return
    for i in V[st]:
        Tree(i)

N = int(input())
cnt = 0
V = [[] for _ in range(N + 1)]
arr = list(map(int, input().split()))
start = []
erase = int(input())
for i in range(N):
    if arr[i] == -1:
        start.append(i)
    elif i == erase:
        continue
    else:
        V[arr[i]].append(i)

for i in start:
    if i != erase:
        Tree(i)
print(cnt)

