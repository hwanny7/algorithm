

# arr = [10, 20, 30, 40]
#
# N = 4
#
# for i in range(0, N):
#     arr[0], arr[i] = arr[i], arr[0]
#     for j in range(1, N):
#         arr[1], arr[j] = arr[j], arr[1]
#         for k in range(2, N):     # range가 1씩 증가
#             arr[2], arr[k] = arr[k], arr[2]
#             print(arr)
#             arr[2], arr[k] = arr[k], arr[2]
#         arr[1], arr[j] = arr[j], arr[1]
#     arr[i], arr[0] = arr[0], arr[i]

# 재귀로 구현
N = 4
arr = [10, 20, 30, 40]

def perm(k):
    if k == N:      #높이가 N이 되면 그만
        print(arr)
        return
    else:
        for i in range(k, N):       #k가 증가하면서
            arr[k], arr[i] = arr[i], arr[k]
            perm(k + 1)
            arr[k], arr[i] = arr[i], arr[k]

perm(0)
