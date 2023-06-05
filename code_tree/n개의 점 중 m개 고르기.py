import math



def combination(start, k, curr_combination):
    global ans

    if k == M:
        print(curr_combination)
        x1, y1 = curr_combination[0]
        x2, y2 = curr_combination[-1]

        ans = min(ans, (x1 - x2) ** 2 + (y1 - y2) ** 2)
        return

    for i in range(start, N):
        combination(i + 1, k + 1, curr_combination + [dot_list[i]])




N, M = map(int, input().split())

dot_list = []

for i in range(N):
    dot_list.append(list(map(int, input().split())))

dot_list.sort()

ans = 0xfffffff
combination(0, 0, [])

print(ans)