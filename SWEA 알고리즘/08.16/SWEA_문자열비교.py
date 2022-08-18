for t in range(1, int(input())+1):
    x = input()
    s = input()
    for i in range(len(s)-len(x)+1):
        if s[i] == x[0]:
            if x == s[i:i+len(x)]:
                print(f'#{t}', 1)
                break
    else:
        print(f'#{t}', 0)



'''
# 교수님 풀이

t = ''; p = ''
m, n = len(p), len(t)

for i in range(n - m + 1):
    for j in range(m):      #패턴의 길이만큼 비교
        if p[j] != t[i + j]:
            break

else:       #패턴이랑 같은 문자를 찾았으면 m만큼 위치를 이동시킨 후 다시 해야 하는데 for 문으로는 i를 바꿀 수 없으니까 while로 진행
    break 

#첫번째 방법
i = 0
while i <= n - m:
    for j in range(m):
        if p[j] != t[i + j]:
            break
            
    else:       #매칭 성공
        i += m - 1
    
    i += 1




'''