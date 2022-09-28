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
#===============prim 1
def prim1(r, V):
    MST = [0] * (V + 1)          #MST 포함여부
    key = [1000] * (V + 1)      #가중치의 최대값 이상으로 초기화
    key[r] = 0                  #시작정점의 key를 0으로, 이미 포함됐기 때문에 비용이 없다.
    for _ in range(V):          #V + 1 개의 정점 중 V 개를 선택
        # MST에 포함되지 않은 정점 중(MST[u] == 0), key가 최소인 u 찾기
        u = 0
        minV = 10000
        for i in range(V + 1):
            if MST[i] == 0 and key[i] < minV:
                u = i
                minV = key[i]
        #=============== MST에 속해있지 않으면서 key 값이 가장 작은 얘
        MST[u] = 1
        # u에 인접인 v에 대해, MST에 포함되어 있지 않은 정점이면
        for v in range(V + 1):
            if MST[v] == 0 and adjM[u][v] > 0:      #MST에 속해있지 않고, 인접해 있으면서(가중치가 있으면 인접해 있는 것임)
                key[v] = min(key[v], adjM[u][v])
    print()
    return sum(key)


V, E = map(int, input().split())
adjM = [[0]* (V + 1) for _ in range(V + 1)]
adjL = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adjM[u][v] = w
    adjM[v][u] = w
    # adjL[u].append((v, w))
    # adjL[v].append((u, w))

print(prim1(0, V))     #0번부터 시작해서 마지막 번호는 V