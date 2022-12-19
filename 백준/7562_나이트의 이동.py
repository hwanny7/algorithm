from collections import deque
import sys
input = sys.stdin.readline

def main():
    N = int(input())
    arr = [[0] * N for _ in range(N)]       # 방문 표시를 할 arr를 설정
    now_c, now_r = map(int, input().split())
    target_c, target_r = map(int, input().split())
    arr[now_c][now_r] = 1        # 처음 위치 방문 표시
    queue = deque()
    queue.append((now_c, now_r))
    # 방향 설정
    dr = [-2,-1,1,2,2,1,-1,-2]
    dc = [1,2,2,1,-1,-2,-2,-1]


    while queue:
            c, r = queue.popleft()
            if [c, r] == [target_c, target_r]:
                print(arr[c][r] - 1)
                break
            for i in range(8):
                nr = dr[i] + r
                nc = dc[i] + c
                if 0 <= nr < N and 0 <= nc < N and arr[nc][nr] == 0:
                    queue.append((nc, nr))
                    arr[nc][nr] = arr[c][r] + 1


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        main()
