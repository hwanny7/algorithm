

# 상어는 방향의 모든 칸으로 이동이 가능. 그 칸의 물고기를 먹고 방향도 가지게 된다.
# 물고기가 없는 칸으로는 이동이 불가능. 이동할 수 있는 칸이 없다면 종료

# 물고기는 번호가 작은 순서대로.
# 빈칸, 다른 물고기가 있는 칸만 이동 가능
# 이동 가능한 칸이 나올 때까지 45도 반시계 회전, 이동할 수 있는 칸이 없다면 이동하지 않는다
# 이동한 칸으로 가면 서로의 위치를 변경한다.

import copy
import sys
input = sys.stdin.readline

dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]

def fish(num):

    if num == 17:
        return


    if not fish_dir[num]:    # 상어한테 잡아 먹혔을 경우
        fish(num + 1)
        return

    c, r, dir = fish_dir[num]    # 해당 숫자 물고기의 현재 위치

    for i in range(dir, dir + 7):
        nc = c + dc[i % 8]
        nr = r + dr[i % 8]
        if 0 <= nc < 4 and 0 <= nr < 4 and arr[nc][nr] != -1:   # 상어가 있는 구역이 아닐 경우
            fish_dir[num] = [nc, nr, i % 8]
            if arr[nc][nr]:     # 빈 공간이 아닌, 물고기가 있는 경우에만
                fish_dir[arr[nc][nr]] = [c, r, fish_dir[arr[nc][nr]][2]]        # 두 숫자 물고기 위치 저장
            arr[c][r], arr[nc][nr] = arr[nc][nr], arr[c][r]                 # arr 에서 숫자 변경
            break

    fish(num + 1)

def shark(c, r, dir, sum):

    global ans, arr, fish_dir



    copy_dir = copy.deepcopy(fish_dir)
    copy_arr = copy.deepcopy(arr)

    fish_dir[arr[c][r]] = []    # 상어가 잡아먹은 물고기 위치 초기화
    arr[c][r] = - 1     # 상어 위치 표시
    fish(1)


    arr[c][r] = 0   # 상어의 이동을 위해서 상어의 현재 위치 지우기

    cnt = 0
    for i in range(1, 4):
        nc = c + dc[dir] * i
        nr = r + dr[dir] * i
        if 0 <= nc < 4 and 0 <= nr < 4 and arr[nc][nr]:
            cnt += 1
            shark(nc, nr, fish_dir[arr[nc][nr]][2], sum + arr[nc][nr])

    # 상어가 먹기 전으로 fish_dir, arr 다 변경해야함
    fish_dir = copy_dir
    arr = copy_arr

    if not cnt:
        ans = max(ans, sum)


arr = []
fish_dir = [[] for _ in range(17)]          #물고기 좌표 저장
ans = 0
for i in range(4):
    temp = list(map(int, input().split()))
    hold = []
    for j in range(0, 8, 2):
        fish_dir[temp[j]] = [i, j // 2, temp[j + 1] - 1]
        hold.append(temp[j])
    arr.append(hold)

shark(0, 0, fish_dir[arr[0][0]][2], arr[0][0])
print(ans)





