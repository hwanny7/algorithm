
N = 10 # 정점수

# disjoint-set

p = [i for i in range(N + 1)]       #make_set()
# find-set(x)
def find_set(x):                    #path compression
    if x != p[x]:   #루트
        p[x] = find_set(p[x])       #루트노드를 찾고 되돌아 오는 과정에서 모든 자식이 루트노드를 가르키도록 바꿔준다.
    return p[x]                     #나중에 바로 루트로 갈 수 있기 때문에 좋다.

# x, y 가 속한 두 집합을 union
a = find_set(x)
b = find_set(y)
if a != b:
    p[a] = b


'''
path compression: find-set을 행하는 과정에서 만나는 모든 노드들이 직접 root를 가리키도록 포인터를 바꿔준다.
'''