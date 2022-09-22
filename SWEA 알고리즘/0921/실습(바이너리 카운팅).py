# arr = [3, 6, 7, 1, 5, 4]
# n = len(arr)
#
#
# for i in range(1, 1<<n):        #공집합을 빼고 만드려면 range를 1부터 시작
#     for j in range(n):
#         if i & (1<<j):
#             print(arr[j], end= ' ')
#
#     print()

#========================================= 다른 방법

def f(i, k):
    if i == k:
        for j in range(k):
            if bit[j]:
                print(arr[j], end = ' ')
        print()
    else:
        bit[i] = 0
        f(i+1, k)
        bit[i] = 1
        f(i+1, k)

arr = [3, 6, 7, 1, 5, 4]
n = len(arr)
bit = [0] * 3
f(0, 3)