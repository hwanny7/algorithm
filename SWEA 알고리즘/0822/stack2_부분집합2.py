# def f(i, N, s, t): # s: 이전까지의 원소 합, t: 찾고자 하는 값
#     global ans
#     global cnt      #호출 횟수 비교
#     cnt += 1
#     if i == N:      #모든 원소가 고려되었고, 부분집합의 합이 t라면 ans += 1
#         if s == t:
#             ans += 1
#         return
#     else:
#         f(i + 1, N, s+A[i], t)      #A[i]번 원소를 포함하기로 했어. 합을 같이 넘겨줄게
#         f(i + 1, N, s, t)           #A[i]가 포함되지 않는 경우
#
#
#
#
# A = [1,2,3,4,5,6,7,8,9,10]
# bit = [0] * 10
# ans = 0
# cnt = 0
# f(0, 10, 0, 10)
# print(ans, cnt)


# def f(i, N):        # 세 칸을 채운다.
#     global ans
#     global cnt
#     cnt += 1
#     if i == N:      #채울 칸의 인덱스랑 채울 칸의 갯수가 같아지면 중단, 0, 1, 2칸까지만 만들면 됨
#         s = 0       # 부분 집합의 합
#         for i in range(N):
#             if bit[i]:  # i가 1일 경우
#                 s += A[i]
#         if s == 10:
#             ans += 1     #부분집합의 합이 10인 경우의 수
#
#     else:
#         candidate = [0, 1]
#         for x in candidate:
#             bit[i] = x
#             f(i + 1, N)
#
# A = [1,2,3,4,5,6,7,8,9,10]
# bit = [0] * 10
# cnt = 0
# ans = 0
# f(0, 10)
# print(ans, cnt)


def f(i, N, s, t): # N: 재귀의 깊이, s: 이전까지의 원소 합, t: 찾고자 하는 값
    global ans
    global cnt      #호출 횟수 비교
    cnt += 1
    if i == N:      #모든 원소가 고려되었고, 부분집합의 합이 t라면 ans += 1
        if s == t:
            ans += 1
        return
    elif s > t:    #지금까지 더해온 값이 이미 t값을 넘었다면
        return     #답은 아니니까 그만해

    else:
        f(i + 1, N, s+A[i], t)      #A[i]번 원소를 포함하기로 했어. 합을 같이 넘겨줄게
        f(i + 1, N, s, t)           #A[i]가 포함되지 않는 경우

A = [1,2,3]
bit = [0] * 3
ans = 0
cnt = 0
f(0, 3, 0, 6)
print(ans, cnt)
