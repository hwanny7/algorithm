# def dfs(S):
#     visited = [0] * N
#     visited[S] = 1
#     queue = [[S, str(S + 1)]]
#     while queue:
#         S, ans = queue.pop(0)
#         for i in range(N):
#             if visited[i]:
#                 continue
#             n = int(arr[i], 2)^int(arr[S], 2)
#             if n & (n - 1) == 0:
#                 temp = ans + str(i + 1)
#                 if i + 1 == end:
#                     return temp
#                 queue.append([i, temp])
#                 visited[i] = 1
#
#
#
# N, K = map(int, input().split())
# arr = [input() for _ in range(N)]
# start, end = map(int, input().split())
#
#
# if start == end:        #시작이랑 끝이 같을 때
#     print(start, end)
# else:
#     ans = dfs(start - 1)
#     if ans:
#         for i in ans:
#             print(i, end=' ')
#     else:
#         print(-1)



def find(S, E):
    visit = 0
    Q = [[S, str(S)]]
    visit |= (1 << S)
    while Q:
        S, ans = Q.pop(0)
        if S == E:
            return ans
        for i in range(1, N + 1):
            if visit & (1 << i):
                continue
            n = int(arr[S], 2)^int(arr[i])
            cnt = 0
            for j in range(K):
                if n & (1 << j):
                    cnt += 1
            if cnt == 1:
                Q.append([i, ans + str(i)])
                visit |= (1 << i)

N, K = map(int, input().split())
arr = [0]
for i in range(N):
    arr.append(input())
start, end = map(int, input().split())
ans = find(start, end)

if ans:
    for i in ans:
        print(i, end = ' ')
elif start == end:
    print(start)
else:
    print(-1)