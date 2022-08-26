def Q():
    global front
    front += 1
    return nums[front]

for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    front = -1
    for i in range(1, M + 1):
        nums[i - 1] = [nums[i - 1], i]

    case = [0] * N
    for i in range(N):      # 화덕에 첫번째 피자 세팅
        case[i] = Q()

    cnt = 0
    front2 = -1     #화덕 프론트
    while cnt != M:
        front2 = (front2 + 1) % N
        if case[front2][0] == 0:
            continue
        case[front2][0] = case[front2][0] // 2
        if case[front2][0] == 0:
            cnt += 1
            if front != M - 1:
                case[front2] = Q()

    print(f'#{t}', case[front2][1])




