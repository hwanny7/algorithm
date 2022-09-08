# cnt = 0
#
#
# def print_hello(i, n):
#     if i == n:
#         global cnt;
#         cnt += 1
#     else:
#         print_hello(i + 1, n)
#         print_hello(i + 1, n)
#
#
# print_hello(0, 3)
# print('cnt = ', cnt)

# def abc(x):
#     print(x, end = ' ')
#     if x == 9:
#         return
#
#     abc(x + 2)
#     print(x, end = ' ')
#
#
# abc(1)

def abc(x):
    print(x)
    # print('#', end=' ')
    if x==2:
        # print('#', end=' ')
        return
    # print('#', end=' ')
    for i in range(2):
        print('#', end='')
        abc(x+1)
        print('#', end='')
    print('#', end='')

abc(0)
#
#
# 3단계
# 누적합 출력하기
# arr=[3,6,3,1,6]

# 3 9 12 13 19 13 12 9 3

# 1.sum을 전역으로 놓고 (global)
# 2.sum을 매개변수로 놓고
# 함수 진입하고 리턴하면서 출력하기