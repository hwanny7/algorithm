def find(now, cnt):
    if now == target:
        print('찾았다!')
        exit(0)







target = int(input())
button = [False] * 10
M = int(input())
broken = list(map(int, input().split()))
for i in range(M):
    button[broken[i]] = True # 고장난 버튼

find(100, 0)