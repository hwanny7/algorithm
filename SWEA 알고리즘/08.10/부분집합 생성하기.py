# # 모든 원소의 경우의 수를 만드는 법
#
# bit = [0, 0, 0, 0]
# for i in range(5):
#     bit[0] = i
#     for j in range(5):
#         bit[1] = j
#         for k in range(5):
#             bit[2] = k
#             for l in range(5):
#                 bit[3] = l
#                 print(bit)       #생성된 부분집합 출력 (부분집합만 출력하는 방법 생각해보기)

#비트연산으로 부분집합 생성하는 방법

arr = [3, 6, 7, 1, 5, 4]   #비트를 6개 준비해야함

n = len(arr)     # n : 원소의 개수

for i in range(1<<n):   # 1<<n : 부분 집합의 개수 (원소가 n개일 경우 모든 부분집합의 수를 의미. 2^n)
    for j in range(n):   #i의 j번 비트를 검사. 원소의 수만큼 비트를 비교한다
        if i & (1<<j):  # i의 j번 비트가 1인 경우 (0이 아니면 다 True)
            print(arr[j], i)   #j번 원소 출력
    print()
print()

'''
'''