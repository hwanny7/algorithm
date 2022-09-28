def find_set(x):
    while x != rep[x]:          #자기 자신을 가르킬 때까지 찾아서 대표원소를 찾는다.
        x = rep[x]
    return x

def union(x, y):
    rep[find_set(y)] = find_set(x)      #뒤에꺼의 대표원소를 찾아서 x를 가르키게 한다.

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

V, E = map(int, input().split())        # V 마지막 정점
edge = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edge.append([u, v, w])
edge.sort(key = lambda x:x[2])
rep = [i for i in range(V + 1)]         # 대표원소 배열

N = V + 1       # 실제 정점의 갯수
cnt = 0         # 선택한 edge의 수
total = 0       # MST 가중치의 합
for u, v, w in edge:
    if find_set(u) != find_set(v):      # 서로 대표원소가 다를 경우
        cnt += 1
        union(u, v)
        total += w
        if cnt == N - 1:    #간선을 다 택했으면
            break

print(total)