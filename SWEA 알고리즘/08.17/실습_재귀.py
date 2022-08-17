
def f(i , N):        #재귀함수의 기본 구조 (i: 현재 단계, N: 목표)

    if i == N:
        print(i)
        return
    else:
        print(i)
        f(i+1, N)

f(0, 3)