adjList = [[1, 2], [0, 3, 4], [0, 4], [1, 5], [1, 2, 5], [3, 4, 6], [5]]




def bfs(v, N): # v 시작정점, N 마지막 정점
    visited = [0] * (N + 1) # visited 생성
    q = []
    q.append(v)     # 시작점 인큐
    visited[v] = 1  # 시작점 처리
    while q:
        v = q.pop(0)
        print(v)
        for w in adjLIst[v]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1     # 우선순위 확인을 위한 숫자 표기

V, e = map(int, input().split())
N = V + 1       # N 정점 개수
adjList = [[] for _ in range(N)]
for _ in range(E):
    a, b= map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)

bfs(0, V)





# 큐가 비어있지 않으면