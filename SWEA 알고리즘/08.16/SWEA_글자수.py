
for t in range(1, int(input())+1):
    x = input()
    y = input()

    max = 0
    for i in x:
        total = 0
        for j in y:
            if i==j:
                total += 1
        if max < total:
            max = total
    print(f'#{t}', max)


'''
교수님 풀이법

for tc in range(1, int(input()) + 1):
    str1 = input()
    str2 = input()
    cnt = [0] * 128     # 아스키코드 값 받을 리스트
    for ch in str2:
        cnt[ord(ch)] += 1
    
    ans = 0
    for ch in str1:
        val = cnt[ord(ch)]
        if ans < val:
            ans = val
    print(ans)




'''