def find(x):

    if box[x]:
        return box[x]

    box[x] = find(x - 1) + find(x - 2) + find(x - 3)
    return box[x]


for t in range(int(input())):
    N = int(input())
    box = [0] * (N + 3)
    box[1] = 1
    box[2] = 2
    box[3] = 4
    print(find(N))
