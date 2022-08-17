import sys; sys.stdin = open('이진탐색.txt')

def binary(key):
    start = 1
    end = P
    count = 0
    while start <= end:
        middle = (start+end) // 2    #인덱스의 중앙값
        count += 1
        if middle == key:
            break
        elif middle > key:
            end = middle
        else:
            start = middle
    return(count)

for t in range(1, int(input())+1):
    P, A, B = map(int, input().split())

    if binary(A) > binary(B):
        print(f'#{t} B')
    elif binary(A) < binary(B):
        print(f'#{t} A')
    else:
        print(f'#{t}', 0)

# P = 400
# key = 50-1
# nums = list(range(P))
# start = 0
# end = P-1
# count = 0
# while start <= end:
#     middle = (start+end) // 2    #인덱스의 중앙값
#     print(middle)
#     count += 1
#     if nums[middle] == key:
#         break
#     elif nums[middle] > key:
#         end = middle - 1
#     else:
#         start = middle + 1
#
# print(count)

