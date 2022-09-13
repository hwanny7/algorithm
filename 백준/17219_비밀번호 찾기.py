import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}
for i in range(N):
    site, password = input().rstrip().split()
    dic[site] = password

for i in range(M):
    site = input().rstrip()
    print(dic[site])
