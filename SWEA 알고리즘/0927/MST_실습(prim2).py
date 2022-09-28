#prim2 가 1보다 간단함
'''
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''
def prim2(r, V):
    MST = [0] * (V + 1)             #mst 포함여부
    MST[r] = 1
    s = 0
    for _ in range(V):
        u = 0
        minV = 10000
        for i in range(V + 1):       #MST에 포함된 정점 i와 인접한 정점 j 중
            if MST[i] == 1:
                for j in range(V + 1):
                    if adjM[i][j] > 0 and MST[j] == 0 and minV > adjM[i][j]:
                        u = j       #처음에는 0과 연결된 정점 중 비용이 제일 작은 정점 2가 연결됨. 다음에는 0과 2의 인접 중 비용이 가장 작은 걸 찾는다.
                        minV = adjM[i][j]

        s += minV

V, E = map(int, input().split())
adjM = [[0]* (V + 1) for _ in range(V + 1)]
adjL = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adjM[u][v] = w
    adjM[v][u] = w
    # adjL[u].append((v, w))
    # adjL[v].append((u, w))

print(prim2(0, V))     #0번부터 시작해서 마지막 번호는 V