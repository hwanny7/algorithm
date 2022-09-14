import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def Tree(v, throw):
    ans[v] = throw

    for i in V[v]:
        if ans[i] == 0:
            Tree(i, v)


N = int(input())

V = [[] for _ in range(N + 1)]
ans = [0] * (N + 1)
for i in range(N - 1):
    p , c = map(int, input().split())
    V[p].append(c)
    V[c].append(p)

Tree(1, 1)
for i in range(2, len(ans)):
    print(ans[i])