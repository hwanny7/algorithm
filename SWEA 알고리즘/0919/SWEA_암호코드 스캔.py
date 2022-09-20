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
    ans = ''
    for i in x:
        n = binary(convert(i))
        ans += '0' * (4 - len(n)) + n

    ratio = []
    first = '1'
    total = 0
    for i in ans.rstrip('0')[::-1]:
        if i == first:
            total += 1
        else:
            ratio.append(total)
            total = 1
            first = i
        if len(ratio) == 4:
            break

    long = len(ans.rstrip('0'))
    m = verify(ans[long - (sum(ratio) * 8) :long], sum(ratio))
    print(m)


def verify(sen, num):
    lst = [[3, 2, 1, 1], [2, 2, 2, 1], [2, 1, 2, 2], [1, 4, 1, 1], [1, 1, 3, 2], [1, 2, 3, 1], [1, 1, 1, 4], [1, 3, 1, 2], [1, 2, 1, 3], [3, 1, 1, 2]]
    ans = []
    for i in range(0, len(sen), num):
        first = '0'
        ratio = []
        total = 0
        for j in sen[i:i+num] + '0':
            if j == first:
                total += 1
            else:
                ratio.append(total)
                total = 1
                first = j
            if len(ratio) == 4:
                for k in range(10):
                    if ratio == lst[k]:
                        ans.append(k)

    one = 0
    two = 0
    for i in range(8):
        if i % 2:
            one += ans[i]
            continue
        two += ans[i]

    return two * 3 + one


for t in range(1, int(input()) + 1):
    N, M = map(int, input().split()) # N = 세로, M = 가로
    arr = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(M -1, -1, -1):
            if arr[i][j] != '0':
                find(arr[i][:j + 1])
                break


# def find(x):
#     ans = ''
#     for i in x:
#         n = binary(convert(i))
#         ans += '0' * (4 - len(n)) + n
#
#     ratio = []
#     first = '1'
#     total = 0
#     for i in ans.rstrip('0')[::-1]:
#         if i == first:
#             total += 1
#         else:
#             ratio.append(total)
#             total = 1
#             first = i
#         if len(ratio) == 4:
#             break
#
#     long = len(ans.rstrip('0'))
#     m = verify(ans[long - (sum(ratio) * 8) :long], sum(ratio))
#     print(m)
#
#
# def verify(sen, num):
#     lst = [[3, 2, 1, 1], [2, 2, 2, 1], [2, 1, 2, 2], [1, 4, 1, 1], [1, 1, 3, 2], [1, 2, 3, 1], [1, 1, 1, 4], [1, 3, 1, 2], [1, 2, 1, 3], [3, 1, 1, 2]]
#     ans = []
#     for i in range(0, len(sen), num):
#         first = '0'
#         ratio = []
#         total = 0
#         for j in sen[i:i+num] + '0':
#             if j == first:
#                 total += 1
#             else:
#                 ratio.append(total)
#                 total = 1
#                 first = j
#             if len(ratio) == 4:
#                 for k in range(10):
#                     if ratio == lst[k]:
#                         ans.append(k)
#
#     one = 0
#     two = 0
#     for i in range(8):
#         if i % 2:
#             one += ans[i]
#             continue
#         two += ans[i]
#
#     return two * 3 + one