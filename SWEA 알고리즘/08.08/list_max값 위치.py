n = int(input())
#최대값의 위치, 같은 값이 있을 때는 맨 오른쪽
arr = list(map(int, input().split()))
maxIdx = 0 # 가정
for i in range(1, N):
    if arr[maxIdx] <= arr [i]:
        maxIdx = i