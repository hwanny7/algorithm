import sys
input = sys.stdin.readline

C, R, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(C)]

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
air = []
Q = set()
for i in range(C):
    for j in range(R):
        if arr[i][j] > 0:
            Q.add((i, j))
        elif arr[i][j] < 0:
            air.append([i, j])

def position(nc, nr, vc, vr, num):
    if (nc == vc or nc == vc + 1) and nr + 1 < R:
        temp[nc][nr + 1] += num
        Q.add((nc, nr + 1))
        return
    if (nc == 0 or nc == C - 1) and 0 <= nr - 1:
        temp[nc][nr - 1] += num
        Q.add((nc, nr - 1))
        return
    #==================================================
    if nr == R - 1 and nc <= vc and 0 <= nc - 1:
        temp[nc - 1][nr] += num
        Q.add((nc - 1, nr))
        return
    if nr == R - 1 and vc + 1 <= nc and nc + 1 < C:
        temp[nc + 1][nr] += num
        Q.add((nc + 1, nr))
        return
    #==================================================
    if nr == 0 and nc + 1 <= vc:
        if temp[nc + 1][nr] == -1:
            return
        temp[nc + 1][nr] += num
        Q.add((nc + 1, nr))
        return
    if nr == 0 and nc - 1 >= vc + 1:
        if temp[nc - 1][nr] == -1:
            return
        temp[nc -1][nr] += num
        Q.add((nc - 1, nr))
        return
    temp[nc][nr] += num


def position_minus(nc, nr, vc, vr, num):
    if (nc == vc or nc == vc + 1) and nr + 1 < R:
        temp[nc][nr + 1] -= num
        Q.add((nc, nr + 1))
        return
    if (nc == 0 or nc == C - 1) and 0 <= nr - 1:
        temp[nc][nr - 1] -= num
        Q.add((nc, nr - 1))
        return
    #==================================================
    if nr == R - 1 and nc <= vc and 0 <= nc - 1:
        temp[nc - 1][nr] -= num
        Q.add((nc - 1, nr))
        return
    if nr == R - 1 and vc + 1 <= nc and nc + 1 < C:
        temp[nc + 1][nr] -= num
        Q.add((nc + 1, nr))
        return
    #==================================================
    if nr == 0 and nc + 1 <= vc:
        if temp[nc + 1][nr] == -1:
            return
        temp[nc + 1][nr] -= num
        Q.add((nc + 1, nr))
        return
    if nr == 0 and nc - 1 >= vc + 1:
        if temp[nc - 1][nr] == -1:
            return
        temp[nc - 1][nr] -= num
        Q.add((nc - 1, nr))
        return
    temp[nc][nr] -= num

vc, vr = air[0]
for cp in range(T):
    temp = [[0] * R for _ in range(C)]
    verify = set()
    for c, r in air:
        temp[c][r] = -1
    for l in range(len(Q)):
        c, r = Q.pop(0)
        num = arr[c][r] // 5
        # temp[c][r] += arr[c][r]           # c,r 과 nc, nr 따로 움직인다.
        position(c, r, vc, vr, num)
        for i in range(4):
            nc = c + dc[i]
            nr = r + dr[i]
            if 0 <= nc < C and 0 <= nr < R and arr[nc][nr] != -1 and num > 0:
                position(nc, nr, vc, vr, num)
                position_minus(c, r, vc, vr, num)
                # temp[nc][nr] += num
                # temp[c][r] -= num



    arr = temp[:]
    for i in temp:
        print(*i)
    print()


#=============================== 두번째 방법
    # dr = [0, 1, 0, -1]
    # dc = [-1, 0, 1, 0]
    # dc2 = [1, 0, -1, 0]
#     c, r = air[0]
#     c2, r2 = air[1]
#     for i in range(4):
#         while True:
#             temp_c = c
#             temp_r = r
#             c = c + dc[i]
#             r = r + dr[i]
#             if air[0][0] < c:
#                 c = temp_c
#                 r = temp_r
#                 break
#             elif 0 <= c < C and 0 <= r < R:
#                 if dic.get((c, r), 0):
#                     if arr[temp_c][temp_r] != -1:
#                         arr[temp_c][temp_r] = dic[(c, r)]
#                         arr[c][r] = 0
#                         Q.append([temp_c, temp_r])
#                         del dic[(c, r)]
#
#                     else:
#                         arr[c][r] = 0
#                         del dic[(c, r)]
#             else:
#                 c = temp_c
#                 r = temp_r
#                 break
#
#             # for k in arr:
#             #     print(*k)
#             # print()
#
#         while True:
#             temp_c = c2
#             temp_r = r2
#             c2 = c2 + dc2[i]
#             r2 = r2 + dr[i]
#             if air[1][0] > c2:
#                 c2 = temp_c
#                 r2 = temp_r
#                 break
#             elif 0 <= c2 < C and 0 <= r2 < R:
#                 if dic.get((c2, r2), 0):
#                     if arr[temp_c][temp_r] != -1:
#                         arr[temp_c][temp_r] = dic[(c2, r2)]
#                         arr[c2][r2] = 0
#                         Q.append([temp_c, temp_r])
#                         del dic[(c2, r2)]
#                     else:
#                         arr[c2][r2] = 0       #그 전이 -1 일 경우 초기화
#                         del dic[(c2, r2)]
#             else:
#                 c2 = temp_c
#                 r2 = temp_r
#                 break
#
#
#
#     for key, value in dic.items():
#         c, r = key
#         arr[c][r] = value
#         Q.append([c, r])
#
# total = 0
# for i in arr:
#     for j in i:
#         if j != -1:
#             total += j
# print(total)


#================================================== 첫번째 방법
#     same_c = []
#     se = []
#     end = []
#     start = []
#     nc, nr = air[0]
#     for key, value in dic.items():      # 에어컨 자리에 있으면 arr 에서 자리 옮기고 stack에 넣기
#         cnt = 0
#         c, r = key
#         if c == nc or c == nc + 1:
#             same_c.append([c, r, value])
#             cnt += 1
#         if c == 0 or c == C - 1:
#             se.append([c, r, value])
#             cnt += 1
#         if r == R - 1:
#             end.append([c, r, value])
#             cnt += 1
#         if r == 0:
#             start.append([c, r, value])
#             cnt += 1
#         if not cnt:
#             arr[c][r] = value
#             Q.append([c, r])
#         #stack에 넣어주기 =====================================
#     same_c.sort(key = lambda x:(x[0],x[1]), reverse = True)
#     se.sort(key = lambda x:(x[0],x[1]))
#     start.sort(key = lambda x: x[0])
#     end.sort(key = lambda x: x[0], reverse = True)
#
#     small_c = []
#     for c, r, value in start:
#         if c < nc:
#             small_c.append([c, r, value])
#         elif arr[c - 1][r] != -1:
#             arr[c - 1][r] = value
#             arr[c][r] = 0
#             Q.append([c - 1, r])
#         else:
#             arr[c][r] = 0
#
#     for c, r, value in small_c[::-1]:
#         if arr[c + 1][r] != -1:
#             arr[c + 1][r] = value
#             arr[c][r] = 0
#             Q.append([c + 1, r])
#         else:
#             arr[c][r] = 0
#
#     for c, r, value in se:              # 2
#         if r - 1 >= 0:
#             arr[c][r] = 0
#             arr[c][r - 1] = value
#             Q.append([c, r - 1])
#
#     small_end = []
#     for c, r, value in end:             # 3번째
#         if nc < c:
#             if c + 1 < C:
#                 arr[c][r] = 0
#                 arr[c + 1][r] = value
#                 Q.append([c + 1, r])
#         else:
#             small_end.append([c, r, value])
#
#     for c, r, value in small_end[::-1]:
#         if c - 1 >= 0:
#             arr[c][r] = 0
#             arr[c - 1][r] = value
#             Q.append([c - 1, r])
#
#
#     for c, r, value in same_c:          # 4번째
#         if r + 1 < R:
#             arr[c][r] = 0
#             arr[c][r + 1] = value
#             Q.append([c, r + 1])
#
# total = 0
# for i in arr:
#     for j in i:
#         if j != -1:
#             total += j
# print(total)