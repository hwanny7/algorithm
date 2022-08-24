
N, M = map(int, input().split())

circle = list(range(1, N + 1))
front = -1
ans = []
cnt = 0
while len(ans) != N:
    front += 1
    if circle[front % N] != 0:
        cnt += 1
    if cnt == M and circle[front % N] != 0:
        ans += [str(circle[front % N])]
        circle[front % N] = cnt = 0

print(f"<{', '.join(ans)}>")
