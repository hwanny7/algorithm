for t in range(1, int(input())+1):
    c, r = map(int, input().split())
    arr = [list(input()) for _ in range(c)]

    result = 0
    for i in range(c): #행
        for j in range(c-r+1): #열
            lst = ''
            lst2 = ''
            for h in range(r): #열에서 문자 길이만큼
                lst += arr[i][j+h]
                lst2 += arr[j+h][i]

            for k in range(r // 2):
                if lst[k] != lst[len(lst)-1-k]:
                    break
            else:
                result += 1
                print(f'#{t}', lst)

            if result == 0:
                for k in range(r // 2):
                    if lst2[k] != lst2[len(lst)-1-k]:
                        break
                else:
                    print(f'#{t}', lst2)