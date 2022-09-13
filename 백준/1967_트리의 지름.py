import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def Tree(V):
    global total
    if not V:
        return
    for i in dis[V]:
        Tree(i)

    temp = []
    if dis[V]:
        for i in dis[V]:
            temp.append(D[i])
        D[V] += max(temp)
        temp.sort(reverse = True)
        temp.append(0)
        if total < temp[0] + temp[1]:
            total = temp[0] + temp[1]

N = int(input())

dis = [[] for _ in range(N + 1)]
D = [0] * (N + 1)

for i in range(N - 1):
    p, c, d = map(int, input().split())
    dis[p].append(c)
    D[c] = d

total = 0
Tree(1)
print(total)
