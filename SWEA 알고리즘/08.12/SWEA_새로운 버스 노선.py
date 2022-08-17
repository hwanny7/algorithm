for T in range(1, int(input())+1):
    station = [0] * 1000
    max = 0
    for t in range(int(input())):
        type, a, b = map(int, input().split())
        if max < b:
            max = b
        check = a % 2
        station[a-1] += 1
        station[b-1] += 1
        if type == 1:
            for s in range(a+1, b):
                station[s-1] += 1
        elif type == 2:
            for s in range(a+2, b, 2):
                station[s-1] += 1
        elif type == 3 and check:   #홀수
            for s in range(a+1, b):
                if s % 3 == 0 and s % 10 != 0:
                    station[s-1] += 1
        else:
            for s in range(a+1, b):
                if s % 4 == 0:
                    station[s-1] += 1
    line = 0
    for i in range(max):
        if line < station[i]:
            line = station[i]
    print(f'#{T}', line)
    print(station)

