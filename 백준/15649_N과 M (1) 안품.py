N = 4
for i in range(1, N+1):
    for j in range(1, N+1):
        if i != j:
            print(i, j)

arr = [1, 2, 3, 4]
N = len(arr)

def perm(k, N):
    if k == N:
        print(arr)
    else:
        for i in range(k, N):
            arr[k], arr[i] = arr[i], arr[k]
            perm(k + 1, N)
            arr[k], arr[i] = arr[i], arr[k]

perm(0, N)

# arr = [1, 2, 3, 4]
# N = len(arr)
# visit = [0] * N  # 요소의 선택 여부 저장
# order = [0] * N  # 실제 순열의 순서를 저장
#
# def perm(k, N):
#     if k == N:
#         print(order)
#     else:
#         for i in range(N):  # 첫번째 요소 선택
#             if visit[i]: continue
#             order[k] = arr[i]
#             visit[i] = 1
#             #---------------------
#             perm(k + 1, N)
#             #---------------------
#             visit[i] = 0
# perm(0, N)
