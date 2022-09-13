# global cnt 없이 순회환 정점 수를 리턴하는 함수
def f(n):
    if n == 0:
        return 0
    else:
        L = f(ch1[n])
        R = f(ch2[n])
        return L + R + 1    # 자기 자신을 더해주기

# return을 통해 높이를 리턴하는 함수

def f(n):
    if n == 0:
        return -1
    else:
        L = f(ch1[n])
        R = f(ch2[n])
        return max(L + R) + 1    # 자기 자신을 더해주기


# 루트 노드 찾기
def find_root(V):
    for i in range(1, V + 1):
        if par[i] == 0:
            return i               #노드를 하나씩 넣어본다.

#이진트리 배열으로 저장했을 때 순회
def pre(n):
    if n <= size:
        print(tree[n])
        pre(2*n)
        pre(2*n + 1)


tree = [0, 'A', 'B', 'C', 'D', 'E', 'F']
size = len(tree) - 1
pre(1)