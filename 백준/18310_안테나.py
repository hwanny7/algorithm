import sys

input = sys.stdin.readline

N = int(input())

arr_x = list((map(int, input().split())))
arr_x.sort()

print(arr_x[(N - 1)// 2])