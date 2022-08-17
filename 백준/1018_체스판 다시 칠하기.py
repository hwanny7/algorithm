
# N, M = map(int, input().split()) # N줄, M행
#
# arr = [list(input()) for _ in range(N)]
#
# g_total = 2500
#
# for c in range(N-7):
#     for r in range(M-7):
#         total = 0
#         total1 = 0
#         for h in range(8):
#             for w in range(8):
#                 if h % 2 == 0:
#                     if w % 2 == 0 and arr[c+h][r+w] != 'W':
#                         total += 1
#                     elif w % 2 == 1 and arr[c+h][r+w] != 'B':
#                         total += 1
#                 else:
#                     if w % 2 == 0 and arr[c+h][r+w] != 'B':
#                         total += 1
#                     elif w % 2 == 1 and arr[c+h][r+w] != 'W':
#                         total += 1
#         for h in range(8):
#             for w in range(8):
#                 if h % 2 == 0:
#                     if w % 2 == 0 and arr[c+h][r+w] != 'B':
#                         total1 += 1
#                     elif w % 2 == 1 and arr[c+h][r+w] != 'W':
#                         total1 += 1
#                 else:
#                     if w % 2 == 0 and arr[c+h][r+w] != 'W':
#                         total1 += 1
#                     elif w % 2 == 1 and arr[c+h][r+w] != 'B':
#                         total1 += 1
#
#         if g_total > total:
#             g_total = total
#         if g_total > total1:
#
# print(g_total)


# 두 가지 방법으로 품

N, M = map(int, input().split()) # N줄, M행

arr = [list(input()) for _ in range(N)]

g_total = 2500

for c in range(N-7):
    for r in range(M-7):
        total = 0
        total1 = 0
        for h in range(8):
            for w in range(8):  # W일떄
                if h == w and arr[c+h][r+w] != 'W':
                    total += 1
                elif h < w and (w-h) % 2 and arr[c+h][r+w] != 'B':
                    total += 1
                elif h < w and (w-h) % 2 == 0 and arr[c + h][r + w] != 'W':
                    total += 1
                elif h > w and (h-w) % 2 and arr[c+h][r+w] != 'B':
                    total += 1
                elif h > w and (h-w) % 2 == 0 and arr[c+h][r+w] != 'W':
                    total += 1

        for h in range(8):   # B일떄
            for w in range(8):
                if h == w and arr[c + h][r + w] != 'B':
                    total1 += 1
                elif h < w and (w-h) % 2 and arr[c + h][r + w] != 'W':
                    total1 += 1
                elif h < w and (w-h) % 2 == 0 and arr[c + h][r + w] != 'B':
                    total1 += 1
                elif h > w and (h-w) % 2 and arr[c + h][r + w] != 'W':
                    total1 += 1
                elif h > w and (h-w) % 2 == 0 and arr[c + h][r + w] != 'B':
                    total1 += 1

        if g_total > total:
            g_total = total
        if g_total > total1:
            g_total = total1

print(g_total)





