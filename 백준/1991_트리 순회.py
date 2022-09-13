def Tree(V):
    if V < 0:
        return
    one[0].append(chr(V + 65))
    Tree(L[V])
    one[1].append(chr(V + 65))
    Tree(R[V])
    one[2].append(chr(V + 65))


N = int(input())

P = [0] * 26
L = [0] * 26
R = [0] * 26

for i in range(N):
    P1, C1, C2 = input().split()
    L[ord(P1) - 65] = ord(C1) - 65
    R[ord(P1) - 65] = ord(C2) - 65

one = [[] for _ in range(3)]
Tree(ord('A') - 65)

for i in range(3):
    print(''.join(one[i]))
