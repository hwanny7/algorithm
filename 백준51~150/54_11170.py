
#
# for i in range(int(input())):     시간초과 뜸
#     h = 0
#     x, y = map(int, input().split())
#     for j in range(x, y+1):
#         count = 0
#         n = j
#         while count < len(str(j)):
#             if n % 10 == 0:
#                 h += 1
#             n //= 10
#             count += 1
#     print(h)

for i in range(int(input())):
    h = 0
    x, y = map(int, input().split())
    for j in range(x, y+1):
        for k in str(j):
            if k == '0':
                h += 1
    print(h)
