# def find_set(x):
#     while x != rep[x]:          #자기 자신을 가르킬 때까지 찾아서 대표원소를 찾는다.
#         x = rep[x]
#     return x
#
# def union(x, y):
#     rep[find_set(y)] = find_set(x)      #뒤에꺼의 대표원소를 찾아서 x를 가르키게 한다.

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

# V, E = map(int, input().split())        # V 마지막 정점
# edge = []
# for _ in range(E):
#     u, v, w = map(int, input().split())
#     edge.append([u, v, w])
# edge.sort(key = lambda x:x[2])
# rep = [i for i in range(V + 1)]         # 대표원소 배열
#
# N = V + 1       # 실제 정점의 갯수
# cnt = 0         # 선택한 edge의 수
# total = 0       # MST 가중치의 합
# for u, v, w in edge:
#     if find_set(u) != find_set(v):      # 서로 대표원소가 다를 경우
#         cnt += 1
#         union(u, v)
#         total += w
#         if cnt == N - 1:    #간선을 다 택했으면
#             break
#
# print(total)

#===================================================================
def find_set(x):
    while x != p[x]:
        x = p[x]
    return x


for tc in range(1, 1 + int(input())):
    N, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    # 간선들 저장
    # 1. 간선들 가중치 오름 차순
    edges.sort(key=lambda x: x[2], reverse=True)
    # disjoin - set 준비
    p = [i for i in range(N + 1)]  # 정점 0에서 N make set
    mst = []  # MST 간선들
    ans = 0  # 가중치 합 누적
    cnt = N   # 정점수 N + 1 개 이므로 MST의 간선 수는 N개
    while cnt:
        u, v, weight = edges.pop()
        a = find_set(u)
        b = find_set(v)
        if a == b:  # 싸이클이 생기는 간선
            continue
        ans += weight
        # mst.append((u, v, weight))
        p[a] = b  # union-set(a,b) 또는 p[b] = a
        cnt -= 1

    print(f'#{tc}', ans)