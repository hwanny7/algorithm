import sys
input = sys.stdin.readline

def dfs(V, D):
    global total
    visited[V] = 1

    dis = []
    for key, value in T[V]:
        if not visited[key]:
            dis.append(dfs(key, value))

    if len(dis) == 0:               #끝 노드일 때
        return D
    else:
        dis.sort(reverse = True)
        dis.append(0)               #자식이 하나밖에 없을수도 있기 때문에 0을 추가
        if total < dis[0] + dis[1]:
            total = dis[0] + dis[1]
        return max(dis) + D         #자식 노드가 있을 때



N = int(input())
T = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
total = 0

for i in range(N):
    arr = list(map(int, input().split()))
    for i in range(1, len(arr), 2):
        if arr[i] == -1:
            break
        T[arr[0]].append((arr[i], arr[i + 1]))

dfs(1, 0)
print(total)


