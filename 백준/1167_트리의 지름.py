import sys
input = sys.stdin.readline

def dfs(v, before):
    global total
    visited[v] = visited[before] + 1
    for i in V[v]:
        if visited[i] == 0:
            dfs(i, v)
    temp = []

    for i in V[v]:
        if visited[i] > visited[v]:
            temp.append(T[v][i])
    if len(temp) >= 1:
        temp.append(0)
        temp.sort(reverse = True)
        if total < temp[0] + temp[1]:
            total = temp[0] + temp[1]
        T[before][v] += temp[0]


N = int(input())
V = [[] for _ in range(N + 1)]
T = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)

for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(1, len(arr)):
        if arr[j] == -1:
            break
        elif j % 2:
            V[arr[0]].append(arr[j])
        else:
            T[arr[0]][arr[j - 1]] = arr[j]

total = 0
dfs(1, 1)
print(total)

