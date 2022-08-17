
for i in range(3):
    nums = list(map(int, input().split()))
    a = nums.count(0)
    b = nums.count(1)
    if a == 4:
        print('D')
    elif b == 4:
        print('E')
    elif a - b == 0:
        print('B')
    elif a == 1:
        print('A')
    else:
        print('C')