N = int(input())
c = [0] * 101  #0부터 100까지 숫자 개수, 0부터 시작하니까 101까지 있어야함
arr = list(map(int, input().split()))

for i in range(N):
    c[arr[i]] += 1
for j in range(1, 101): # 개수 누적
    c[j] += c[j-1]

tmp = [0] * N

for i in range(N-1, -1, -1): #원본을 뒤에서부터
    c[arr[i]] -= 1
    tmp[c[arr[i]]] = arr[i]

print(tmp)