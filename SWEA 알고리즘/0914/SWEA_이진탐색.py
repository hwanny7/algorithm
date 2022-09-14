def Tree(V):
    global cnt
    if N < V:
        return
    Tree(V * 2)
    cnt += 1
    home[V] = cnt
    Tree(V * 2 + 1)

for t in range(1, int(input()) + 1):
    cnt = 0
    N = int(input())
    home = [0] * (N + 1)
    Tree(1)
    print(f'#{t}', home[1], home[N // 2])