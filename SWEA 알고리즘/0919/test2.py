# import sys; sys.stdin = open('input.txt')

binary = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
          '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111',
          }


def find(x):
    global grand
    ans = ''
    for i in x:
        ans += binary[i]

    ans = ans.rstrip('0')


    v = []

    ratio = []
    total = 0
    first = '1'
    for i in range(len(ans) - 1, -1, -1):
        if ans[i] == first:
            total += 1
        elif len(ratio):
            ratio.append(total)
            total = 1
            first = ans[i]
        else:
            first = '1'
            total = 0
            ratio = []
            small = min(ratio)
            temp = (ratio[2] // small, ratio[1] // small, ratio[0] // small)
            v.append(lst[temp])

        if len(v) == 8:
            if v not in V:
                m = (v[1] + v[3] + v[5] + v[7]) * 3 + v[0] + v[2] + v[4] + v[6]
                if m % 10 == 0:
                    grand += sum(v)
                V.append(v)
            v = []










for t in range(1, int(input()) + 1):
    lst = {(2, 1, 1): 0, (2, 2, 1): 1, (1, 2, 2): 2, (4, 1, 1): 3, (1, 3, 2): 4, (2, 3, 1): 5, (1, 1, 4): 6,
           (3, 1, 2): 7, (2, 1, 3): 8, (1, 1, 2): 9}
    N, M = map(int, input().split())  # N = 세로, M = 가로
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