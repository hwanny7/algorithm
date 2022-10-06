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
def prim1(r, V):                # 양방향 간선일 때는 마지막 노드도 포함시켜야 하고, 아닐 경우 굳이 포함시킬 필요 없음
    MST = [0] * (V + 1)         #트리에 포함된 녀석들
    key = [1000] * (V + 1)      #가중치의 최대값 이상으로 초기화
    key[r] = 0                  #시작정점의 key를 0으로, 이미 포함됐기 때문에 비용이 없다.
    for _ in range(V):          #V + 1 개의 정점 중 V 개를 선택해서 값을 갱신한다.
        # MST에 포함되지 않은 정점 중(MST[u] == 0), key가 최소인 u 찾기
        u = 0   #인덱스 값
        minV = 10000
        for i in range(V + 1):
            if MST[i] == 0 and key[i] < minV:               # 간선의 최소값 찾는 과정을 우선순위 큐로 구현하면 더 빨라진다.
                u = i
                minV = key[i]
        #=============== MST에 속해있지 않으면서 key 값이 가장 작은 얘
        MST[u] = 1
        # u에 인접인 v에 대해, MST에 포함되어 있지 않은 정점이면
        for v in range(V + 1):
            if MST[v] == 0 and adjM[u][v] > 0:      #MST에 속해있지 않고, 인접해 있으면서(가중치가 있으면 인접해 있는 것임) / 속해있는 것을 연결하면 루프가 되기 때문에 꼭 MST 여부를 확인해야 함
                key[v] = min(key[v], adjM[u][v])
        # 트리에 포함되지 않은 얘 중에서 새로운 간선을 선택하기 때문에 cicle이(루프) 생길 일이 없다.

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