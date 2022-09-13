N = int(input())
M = [64]
while sum(M) != N:
    M[-1] = M[-1] // 2
    if sum(M) > N:
        continue
    elif sum(M) < N:
        M.append(M[-1])

print(len(M))

