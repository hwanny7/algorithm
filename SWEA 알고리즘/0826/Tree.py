'''
13 12
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

V, E = map(int, input().split())
arr = list(map(int, input().split()))

L = [0] * (V + 1)       #노드 번호가 1번부터 V번까지 있을 경우 (0번 인덱스는 공란)
R = [0] * (V + 1)       #오른쪽 자식을 위한 배열
P = [0] * (V + 1)       #부모도 저장하고 싶으면

for i in range(0, E*2, 2):      #간선을 두칸씩 점프하면서
    parent, child = arr[i], arr[i + 1]
    if L[parent] == 0:      #parent 자식 정보가 처음 들어오는구나
        L[parent] = child
    else:
        R[parent] = child
    P[child] = parent       #부모도 저장하고 싶으면

def inorder(v):
    if v == 0:              #여기가 끝이기 때문에 돌아가
        return
    # 전위 순회
    print(v, end=' ')       #여기서 방문을 하면 전위 순회
    inorder(L[v])           #무조건 왼쪽 자식부터
    # 중위 순회
    print(v, end = ' ')     #방문은 내가 하고 싶은 일. 하고 싶은 일에 따라 순서를 다르게 해야 한다.
    inorder(R[v])
    # 후위 순회
inorder(1)      #루트는 순회할 때 시작점을 얘기함. 보통 1번
