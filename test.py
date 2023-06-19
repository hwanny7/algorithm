N = 4
print(1 << (N))

for i in range(1, 1 << N):
	a, b = [], []
	for j in range(N):
		if (1 << j) & i:
			a.append(j)
		else:
			b.append(j)
