
for t in range(int(input())):
    car = int(input())

    for i in range(int(input())):
        x, y = map(int, input().split())
        car += x*y

    print(car)
