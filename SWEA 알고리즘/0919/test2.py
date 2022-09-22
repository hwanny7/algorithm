# import sys; sys.stdin = open('input.txt')

def binary(x):
    if x <= 1:
        return str(x)
    return binary(x // 2) + str(x % 2)

def convert(x):
    dic = {'A':10, 'B':11, 'C':12, 'D': 13, 'E':14, 'F':15}
    if x in dic:
        return dic[x]
    return int(x)


def verify(sen, num):
    global grand
    ans = []
    for i in range(0, len(sen), num):
        first = '0'
        ratio = []
        total = 0
        for j in sen[i:i+num] + '0':
            if j == first:
                total += 1
            else:
                ratio.append(total // (num // 7))
                total = 1
                first = j
            if len(ratio) == 4:
                for k in range(10):
                    if ratio == lst[k]:
                        ans.append(k)

    one = 0
    two = 0

    if not ans:
        return

    for i in range(8):
        if i % 2:
            one += ans[i]
            continue
        two += ans[i]

    if (two * 3 + one) % 10 == 0:
        grand += sum(ans)

def find(x):
    ans = ''
    for i in x:
        n = binary(convert(i))
        ans += '0' * (4 - len(n)) + n

    print(ans)

    ans = ans.rstrip('0')
    long = len(ans)

    ratio = []
    first = '1'
    total = 0

    for i in range(long - 1, -1, -1):
        if ans[i] == first:
            total += 1
        elif ans[i] == '0' and len(ans) == 0:
            continue
        else:
            ratio.append(total)
            total = 1
            first = ans[i]
        if len(ratio) == 4:
            total = 0
            first = '1'
            L = long - sum(ratio) * 8
            if ans[L:long] in humm:
                ratio = []
                long = L
                continue
            humm.append(ans[L:long])
            verify(ans[L:long], sum(ratio))
            ratio = []
            long = L



for t in range(1, int(input()) + 1):
    humm = []
    lst = [[3, 2, 1, 1], [2, 2, 2, 1], [2, 1, 2, 2], [1, 4, 1, 1], [1, 1, 3, 2], [1, 2, 3, 1], [1, 1, 1, 4],
           [1, 3, 1, 2], [1, 2, 1, 3], [3, 1, 1, 2]]
    N, M = map(int, input().split()) # N = 세로, M = 가로
    arr = []
    for i in range(N):
        N = input().strip().rstrip('0')
        if len(N) and N not in arr:
            arr.append(N)          #여기서 2진수로 변환

    grand = 0
    for i in range(len(arr)):
        find(arr[i])
    print(f'#{t}', grand)