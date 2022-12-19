arr = [(3, 1), (2, 1), (5, 2), (5, 4)]

c, r = sorted(arr, key = lambda x: (x[0], x[1]))[0]
print(c, r)