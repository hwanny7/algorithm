

'''
0번부터 N번까지, E개의 간선
6 8
0 1
0 2
1 3
1 4
2 4
3 5
4 5
5 6
'''

#재귀방법과 간선 만들기

def dfs(v):
    print(v)        # 방문 표시
    visited[v] = 1
    for w in adjList[v]:
        if visited[w] == 0:     # 방문하지 않은 w니까 이동한다.
            dfs(w)              # 바로 이동하고 만약 갈 수 있는 곳이 없는 지점까지 가면 재귀로 돌아가면서 stack에서 새로운 w를 찾는 것처럼 동일한



V, E = map(int, input().split())
N = V + 1       # 노드가 0~6까지 있으니까 7개이다.
adjList = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adjList[a].append(b)    # 0과 1이 서로 연결되어 있으면 (0, 1) (1, 0)등 양방향을 고려해서 생성해줘야함
    adjList[b].append(a)
print(adjList)
visited = [0] * N

dfs(0)