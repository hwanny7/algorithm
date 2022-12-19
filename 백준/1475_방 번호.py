

nums = list(map(int, input()))
visit = [0] * 10

for i in nums:
    if i == 6 or i == 9:
        if visit[6] <= visit[9]:
            visit[6] += 1
        else:
            visit[9] += 1
    else:
        visit[i] += 1

print(max(visit))