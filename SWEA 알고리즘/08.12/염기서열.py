
p = 'CAT'
t = 'ATTTGTGCATGTTTGAGCTCATTCCTGCGCGCCCGGGGTTTT'
n, m = len(p), len(t)
#텍스트에서 패턴이 존재할 수 있는 모든 시작 위치
for i in range(n - m + 1):    # 0 ~ n-m
    # i = 매칭할 텍스트의 시작위치
    for j in range(m):      # 0 ~ m-1
        if p[j] != t[i + j]:
            break
    else:
        print(i, t[i:i + m])
        break

