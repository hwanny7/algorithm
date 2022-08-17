
for t in range(1, int(input())+1):
    x = input()
    y = input()

    max = 0
    for i in x:
        total = 0
        for j in y:
            if i==j:
                total += 1
        if max < total:
            max = total
    print(f'#{t}', max)
