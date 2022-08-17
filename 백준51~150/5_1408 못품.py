x, y, z = map(int, input().split(':'))
a, b, c = map(int, input().split(':'))

print(x, y, z, a, b, c)
i = x*3600+y*60+z
j = a*3600+b*60+c
print(i, j)

print(f'{((j - i) // 3600) % 24 }:{((j - i) % 3600) // 60}:{((j - i) % 3600) % 60}')