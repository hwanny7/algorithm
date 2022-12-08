# import sys
# input = sys.stdin.readline
#
# def dfs(x):
#     global cnt
#     visit[x] = False
#
#     for i in Tree[x]:
#         if visit[i]:
#             cnt += 1
#             dfs(i)
#
#
# for t in range(int(input())):
#     cnt = 0
#     N, F = map(int, input().split())
#     Tree = [[] for _ in range(N + 1)]
#     visit = [True] * (N + 1)
#     for i in range(F):
#         S, E = map(int, input().split())
#         Tree[S].append(E)
#         Tree[E].append(S)
#     dfs(1)
#     print(cnt)


import sys
lines = sys.stdin.readlines()
T = int(lines[0])
i = 0
ret = []
for t in range(T):
    i += 1
    N, M = [ int(s) for s in lines[i].split() ]
    ret.append(str(N-1))
    i += M
print('\n'.join(ret))






# def find(x):
#     if V[x] == x:
#         return x
#     return find(V[x])
#
#
# for t in range(1, int(input()) + 1):
#     people, paper = map(int, input().split())
#     arr = list(map(int, input().split()))
#     V = [i for i in range(people + 1)]
#     for i in range(0, paper * 2, 2):
#         V[find(arr[i])] = V[find(arr[i + 1])]
#
#     ans = 0
#     for j in range(1, people + 1):
#         if j == V[j]:
#             ans += 1
#     print(V)
#     print(f'#{t}', ans)