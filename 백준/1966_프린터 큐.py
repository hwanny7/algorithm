

for t in range(int(input())):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    arr = []
    for i in range(N):
        arr.append((nums[i], i))    # 값이랑 idx번호 arr에 저장

    idx = 0                         # 비교 기준이 될 idx 번호
    while idx < N-1:                # 인덱스가 N-1이 됐을 때 중지
        max = arr[idx][0]           # 초기 max값은 기준 인덱스로
        for i in range(idx+1, N):   # 기준 인덱스 뒤에 있는 애들 중에 큰 값 찾기
            if max < arr[i][0]:
                arr.append(arr.pop(idx))
                break
        else:
            idx += 1                # 기준 인덱스보다 큰 게 없으면 기준 인덱스를 다음껄로 옮기기

    for i in range(N):
        if arr[i][1] == M:
            print(i+1)