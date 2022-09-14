def Tree(v):
    if left[v]:
        l = Tree(left[v])
        r = Tree(right[v])
        if V[v] == '+':
            return l + r
        elif V[v] == '-':
            return l - r
        elif V[v] == '*':
            return l * r
        elif V[v] == '/':
            return l / r
    else:
        return int(V[v])

for t in range(1, 11):
    N = int(input())
    V = [0] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    for i in range(N):
        arr = list(input().split())
        V[int(arr[0])] = arr[1]
        if len(arr) == 4:
            left[int(arr[0])] = int(arr[2])
            right[int(arr[0])] = int(arr[3])

    print(f'#{t}', int(Tree(1)))