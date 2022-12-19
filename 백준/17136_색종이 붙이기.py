# import sys
# input = sys.stdin.readline
#
# def set(i = 0, total = 0):
#     global real_ans
#     if 25 - (paper[1] + paper[2] + paper[3] + paper[4] + paper[5]) > real_ans:
#         return
#     if i == len(one):
#         if total == len(one):
#             ans = 0
#             for i in paper:
#                 if i != 5:
#                    ans += 5 - i
#             if ans < real_ans:
#                 real_ans = ans
#         return
#
#     c, r = one[i]
#     if arr[c][r] == 0:
#         set(i + 1, total)
#     else:
#         nums = check(c, r)
#         for n in nums:
#             if paper[n + 1] == 0:
#                 continue
#             paper[n + 1] -= 1
#             cnt = 0
#             for nc, nr in one:
#                 if c <= nc <= c + n and r <= nr <= r + n:
#                     arr[nc][nr] = 0
#                     cnt += 1
#             set(i + 1, total + cnt)
#             for nc, nr in one:
#                 if c <= nc <= c + n and r <= nr <= r + n:
#                     arr[nc][nr] = 1
#             paper[n + 1] += 1
#
#
# def check(c, r):
#     nums = [0]
#     for i in range(1, 5):
#         if c + i < 10 and r + i < 10:
#             cnt = 0
#             for nc, nr in one:
#                 if c <= nc <= c + i and r <= nr <= r + i:
#                     if arr[nc][nr] != 0:
#                         cnt += 1
#             else:
#                 if cnt == (i + 1) ** 2:
#                     nums.append(i)
#     return nums



# arr = [list(map(int, input().split())) for _ in range(10)]
#
# one = []
# total = 0
# paper = [5] * 6
# for i in range(10):
#     for j in range(10):
#         if arr[i][j]:
#             one.append([i, j])
#             total += 1
# real_ans = 26
# set()
# if real_ans == 26:
#     print(-1)
# else:
#     print(real_ans)

import sys
input = sys.stdin.readline

def set(i = 0, total = 0, p = 0):
    global real_ans, count
    if p >= real_ans:
        return
    count += 1
    if i == len(one):
        if total == len(one):
            real_ans = min(real_ans, p)
        return

    c, r = one[i]
    if arr[c][r] == 0:
        set(i + 1, total, p)
    else:
        nums = check(c, r)
        for n in nums:
            if paper[n + 1] == 0:
                continue
            paper[n + 1] -= 1
            cnt = 0
            for nc, nr in one:
                if c <= nc <= c + n and r <= nr <= r + n:
                    arr[nc][nr] = 0
                    cnt += 1
            set(i + 1, total + cnt, p + 1)
            for nc, nr in one:
                if c <= nc <= c + n and r <= nr <= r + n:
                    arr[nc][nr] = 1
            paper[n + 1] += 1


def check(c, r):
    nums = []
    for i in range(4, 0, -1):
        if c + i < 10 and r + i < 10:
            cnt = 0
            for nc, nr in one:
                if c <= nc <= c + i and r <= nr <= r + i:
                    if arr[nc][nr] != 0:
                        cnt += 1
            else:
                if cnt == (i + 1) ** 2:
                    nums.append(i)
    else:
        nums.append(0)
        return nums



arr = [list(map(int, input().split())) for _ in range(10)]

one = []
total = 0
paper = [5] * 6
for i in range(10):
    for j in range(10):
        if arr[i][j]:
            one.append([i, j])
            total += 1
real_ans = 26
count = 0
set()
if real_ans == 26:
    print(-1)
else:
    print(real_ans, count)