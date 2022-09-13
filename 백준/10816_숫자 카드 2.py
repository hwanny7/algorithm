import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dic = {}
for i in range(N):
    dic[arr[i]] = dic.get(arr[i], 0) + 1

M = int(input())
arr_2 = list(map(int, input().split()))
for i in range(M):
    print(dic.get(arr_2[i], 0), end = ' ')