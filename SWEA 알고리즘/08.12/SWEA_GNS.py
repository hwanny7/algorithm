import sys; sys.stdin = open('GNS_test_input.txt','r')

# def chr(s):
#     lst = ['ZR', 'ON', 'TW', 'TH', 'FO', 'FI', 'SI', 'SV', 'EG', 'NI']
#     for i in range(len(lst)):
#         if s[0]+s[1] == lst[i]:
#             return i

for i in range(1, int(input()) + 1):
    N, M = map(str, input().split())
    nums = list(input().split())

    dic = {'ZRO': 0, 'ONE': 0, 'TWO': 0, 'THR': 0, 'FOR': 0, "FIV": 0, 'SIX': 0, 'SVN': 0, 'EGT': 0, 'NIN': 0}

    for j in nums:
        dic[j] += 1
    print(N)
    for key, value in dic.items():
        for values in range(value):
            print(key, end=' ')
    print()


    # case = [0]* 10
    # for i in nums:
    #     case[chr(i)] += 1
    #
    # print(case)



