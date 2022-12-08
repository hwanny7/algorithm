
N = int(input())
timeTable = [0] * N
for i in range(N):
    math = list(map(int, input().split()))
    start = 0
    for j in math[1:]:
        start = start | (1 << j)
    timeTable[i] = start

student = int(input())
for i in range(student):
    math = list(map(int, input().split()))
    start = 0
    for i in math[1:]:
        start = start | (1 << i)
    ans = 0
    for i in timeTable:
        if (i & start) == i:
            ans += 1
    print(ans)

