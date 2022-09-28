'''
6 8     마지막 정점번호(0번부터 시작), E 간선 수
0 1 0 2 0 5 0 6 4 4 3 5 6 3 5 4

'''

V, E = map(int, input().split())
arr = list(map(int, input().split()))
#인접행렬
adj = [[0] * (V + 1) for _ in range(V + 1)]
adjlist = [[] for _ in range(V + 1)]

for i in range(E):
    n1, n2 = arr[i * 2], arr[i * 2 + 1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1         #방향이 없는 경우 (양방향)
    adjlist[n1].append(n2)
    adjlist[n2].append(n1)

print()