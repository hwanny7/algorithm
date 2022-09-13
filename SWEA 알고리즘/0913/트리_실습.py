
'''
13 12
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
5
3

트리 순회 연습


전/중/후위 순회
트리의 높이를 계산.

1이 루트인 트리의 높이 --> 4
3이 루트인 트리의 높이 --> 3


높이가 3인 노드들 찾기.

(7, 8, 9, 10, 11)


3번 노드가 루트인 트리의 전체 노드수를 계산.

8 개


8번 노드와 10번 노드의 공통조상을 찾기.

(1, 3)

'''

#내가 작성한 것
def Tree(v, h):
    global height
    global cnt
    cnt += 1
    for i in V[v]:
        Tree(i, h + 1)
    if height < h:
        height = h
    if h == find_h:
        print(v, end = ' ')




N, M = map(int, input().split())
V = [[] for _ in range(N + 1)]
P = [0] * (N + 1)
arr = list(map(int, input().split()))
for i in range(0, M * 2, 2):
    V[arr[i]].append(arr[i + 1])
    P[arr[i + 1]] = arr[i]
cnt = 0
node = int(input())
find_h = int(input())
height = 0
Tree(node, 0)
print()
print('height = ', height, 'cnt = ', cnt)
same = (8, 10)
lst = []
for i in same:
    while P[i] != 0:
        i = P[i]
        if i in lst:
            print('조상노드', i)
        lst.append(i)
