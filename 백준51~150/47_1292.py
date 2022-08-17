
x, y = map(int, input().split())

lst = []
count = 1
total = 0
while total <= y:
    for i in range(count):
        lst.append(count)
    total += count    #카운팅의 누적합만큼 길이가 늘어난다.
    count += 1

print(sum(lst[x-1:y]))

