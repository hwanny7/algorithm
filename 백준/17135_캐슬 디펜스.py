import copy
def find(start = 0, lst = []):
    global ans
    if len(lst) == 3:
        end = 0
        many = 0
        dic2 = copy.deepcopy(dic)
        while end != enemy:
            kill = []
            for i in lst:
                dis = 0xfffffffff
                small = [0, 0]     #층, 가로
                for stair in range(C - 1, - 1, -1):
                    for key in dic2[stair]:
                        temp = abs(C - stair) + abs(i - key)
                        if temp > D:
                            continue
                        if dis > temp or (dis == temp and small[1] > key):
                            dis = temp
                            small[0] = stair
                            small[1] = key

                if dis != 0xfffffffff:
                    kill.append(small)

            for stair, key in kill:
                try:
                    dic2[stair].remove(key)
                    many += 1
                    end += 1
                except:
                    pass

            end += len(dic2[C - 1])
            for stair in range(C - 2, -1, -1):
                dic2[stair + 1] = dic2[stair]
            dic2[0] = []

        ans = max(ans, many)
        return

    for i in range(start, R):
        find(i + 1, lst + [i])


C, R, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(C)]

dic = {}
enemy = 0
for i in range(C):
    dic[i] = []
    for j in range(R):
        if arr[i][j]:
            enemy += 1
            dic[i].append(j)

ans = 0
find()
print(ans)