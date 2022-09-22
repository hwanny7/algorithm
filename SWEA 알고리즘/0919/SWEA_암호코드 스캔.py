import sys; sys.stdin = open('input.txt')

def binary(x):
    if x <= 1:
        return str(x)
    return binary(x // 2) + str(x % 2)

def convert(x):
    dic = {'A':10, 'B':11, 'C':12, 'D': 13, 'E':14, 'F':15}
    if x in dic:
        return dic[x]
    return int(x)


def find(x):
    global grand
    ans = ''
    for i in x:
        n = binary(convert(i))
        ans += '0' * (4 - len(n)) + n

    ans = ans.rstrip('0')
    long = len(ans)
    # print(ans)

    v = []

    while long >= 0:
        j = 1
        if ans[long - j] != '1':
            long -= 1
            continue

        ratio = []
        first = '1'
        total = 0
        while len(ratio) != 3:
            if ans[long - j] == first:
                total += 1
            else:
                ratio.append(total)
                total = 1
                first = ans[long - j]
            j += 1

        small = min(ratio)
        temp = (ratio[2] // small, ratio[1] // small, ratio[0] // small)

        v.append(lst[temp])
        long -= (7 - sum(temp)) * small + sum(ratio)

        if len(v) == 8 and v not in V:
            m = (v[1] + v[3] + v[5] + v[7]) * 3 + v[0] + v[2] + v[4] + v[6]
            if m % 10 == 0:
                grand += sum(v)
            V.append(v)
            v = []
        elif len(v) == 8:
            v = []



for t in range(1, int(input()) + 1):
    lst = {(2, 1, 1):0, (2, 2, 1):1, (1, 2, 2):2, (4, 1, 1):3, (1, 3, 2):4, (2, 3, 1):5, (1, 1, 4):6,
           (3, 1, 2):7, (2, 1, 3):8, (1, 1, 2):9}
    N, M = map(int, input().split()) # N = 세로, M = 가로
    V = []
    arr = []
    for i in range(N):
        N = input().strip().rstrip('0')
        if len(N) and N not in arr:
            arr.append(N)

    grand = 0
    for i in range(len(arr)):
        find(arr[i])

    print(f'#{t}', grand)