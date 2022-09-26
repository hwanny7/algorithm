def f2(i, k, t, s, rs):
    if i == k:
        if t == s:              #합계가 구하고자 하는 값과 같으면
            for j in range(10):
                if bit[j]:
                    print(A[j], end= ' ')
    elif t <= s:
        return
    elif t > s + rs:            #남은 수의 합계와 S를 더해도 t 가 큰 경우 다시 후보군을 선정해야 하니까 되돌아가기
        return
    else:
        bit[i] = 0              #포함하지 않을 때
        f2(i + 1, k, t, s, rs - A[i])
        bit[i] = 1              #포함 할 때
        f2(i + 1, k, t, s+A[i], rs - A[i])

A = [i for i in range(1, 11)]
bit = [0] * 10
f2(0, 10, 54, 0, sum(A))
