def f(i, N):
    if i == N:
        print(p)        #작업 끝
    else:
        for j in range(i, N):           # P[i]에 들어갈 숫자 결정 p[j]결정
            p[i], p[j] = p[j], p[i]
            f(i + 1, N)                 # 다음 자리를 만들러 가봐
            p[i], p[j] = p[j], p[i]     #원상복귀


p = [1,2,3]
f(0, 3)     #사전상 순서로 만들어지진 않지만, 모든 경우의 수가 나타난다.