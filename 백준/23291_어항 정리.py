#
#
# # 고유번호를 붙일 필요없이 가장 많은 것과 적은 것만 알면 된다.
# # 물고기의 갯수는 같을 수 있음. 최소와 최대가 1개 이상일 가능성
#
# # 1. 물고기의 수가 가장 적은 어항에 물고기를 한 마리 넣는다.
# # min 과 index를 통해서
# # index 찾기로 적은 물고기 찾기 (while 문)
#
# # 2. 가장 왼쪽에 있는 어항을 그 어항의 오른쪽 위에 쌓는다. (불가능할 때까지)
# # > 쌓기 전에 일자로 늘어놓기 때문에 처음에는 하나씩 올라간다. 2의^n 만큼 상자가 증가하게 된다.
# # 어항이 짝수개로 주어지기 때문에 언제 끝내야 하는지 계산할 수 있다
# # 한방에 달팽이 만들듯이 만들기
#
# # 3. 물고기 수 조절
# # 인접한 두 어항의 차이를 몫으로 나누고 많은 곳에서 적은 곳으로 이동 (동시 발생)
# # dfs, bfs를 사용
#
# # 4. 다시 어항을 일렬로 놓는다.
#
# # 5. 다시 공중부양 N/2 개를.. 어항의 수는 양수이고, 물고기가 완전히 줄어드는 경우는 없음
# # 이 작업은 두 번 하면 바닥에 어항의 수는 N/4개가 된다.
#
# # 6. 다시 물고기 조절 작업을 수행하고, 바닥에 일렬로 놓는 작업을 수행
#
# # 만들어야 할 함수
# # 물고기를 한 개씩 추가하는 함수
# # 어항을 쌓으면서 90도 눕히는 함수
# # 물고기를 교환하는 함수 (최소, 최대 구하기, 최소 최대 차이 확인)
# # 어항을 일렬로 놓는 함수

import sys
input = sys.stdin.readline

def count(small):   # 물고기 한개씩 채우기
    try:
        index = arr.index(small)
        arr[index] += 1
        count(small)

    except:
        return

def angle(lst, floor):   #long 현재 가로
    high = len(lst)
    new = []
    if high <= N - floor:   # 현재 높이만큼 남은 바닥이 있는 경우
        for i in range(len(lst[0])):
            temp = []
            for j in range(high - 1, -1, -1):
                temp.append(lst[j][i])
            new.append(temp)
        new.append(arr[floor:floor + high])

        return angle(new, floor + high)

    else:       # 다음 바닥이 없는 경우
        extra = N - floor
        lst[-1].extend(arr[floor::])
        for i in range(high - 1):
            lst[i].extend([0] * extra)

        return lst


def plus(lst):
    M = len(lst)    # 높이
    R = len(lst[0]) # 가로
    visit = [[0] * R for _ in range(M)]

    dr = [0, 1]     # 하, 우만 확인
    dc = [1, 0]

    for i in range(M):
        for j in range(R):
            if lst[i][j]:
                visit[i][j] += lst[i][j]
                for k in range(2):
                    nc = i + dc[k]
                    nr = j + dr[k]
                    if 0 <= nc < M and 0 <= nr < R and lst[nc][nr]:
                        diff = abs(lst[i][j] - lst[nc][nr]) // 5
                        if lst[nc][nr] > lst[i][j]:
                            visit[nc][nr] -= diff
                            visit[i][j] += diff
                        else:
                            visit[i][j] -= diff
                            visit[nc][nr] += diff

    return visit

def flat(lst):
    C = len(lst)    # 높이
    R = len(lst[0]) # 가로
    new = []
    for r in range(R):
        for c in range(C - 1, -1, -1):
            if lst[c][r]:
                new.append(lst[c][r])

    return new
def fly(lst):
    R = len(lst) // 2 # 가로
    new = []
    new.append(lst[:R][::-1])
    new.append(lst[R:])

    R = R // 2


    new2 = []
    for i in range(1, -1, -1):
        new2.append(new[i][:R][::-1])
        new[i] = new[i][R:]

    new2.extend(new)
    return new2





N, K = map(int, input().split())    # 어항의 수 ( N은 4 이상, 4의 배수), K개 이하
arr = list(map(int, input().split()))
cnt = 0
while True:    # 차이가 K개 이하가 될 때까지
    small, big = min(arr), max(arr)
    if big - small <= K:
        print(cnt)
        break
    count(small)
    arr = flat(plus(fly(flat(plus(angle([[arr[0]]], 1))))))
    cnt += 1
