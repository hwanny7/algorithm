# for t in range(1, int(input()) + 1):
#     N, num = input().split()
#     ans = []
#     N = int(N)
#     print(f'#{t} ', end='')
#     for i in range(N):
#         a = int(num[i], 16)
#         ans = format(a, 'b')
#         print('0' * (4 - len(ans)) + ans, end='')
#     print()

def binary(x):
    if x <= 1:
        return str(x)
    return binary(x // 2) + str(x % 2)
def convert(x):
    dic = {'A':10, 'B':11, 'C':12, 'D': 13, 'E':14, 'F':15}
    if x in dic:
        return dic[x]
    return int(x)

for t in range(1, int(input()) + 1):
    N, num = input().split()
    print(f'#{t}', end=' ')
    for i in num:
        temp = binary(convert(i))
        print('0' * (4 - len(temp)) + temp, end = '')
    print()

