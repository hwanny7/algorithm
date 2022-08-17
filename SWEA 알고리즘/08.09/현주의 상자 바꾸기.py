for t in range(1 , int(input())+1):
    X , Y = map(int, input().split())
    nums = [0] * X
    for y in range(1, Y+1):
        a, b = map(int, input().split())
        for i in range(a-1, b):
            nums[i] = y

    print(f'#{t}')
    for num in nums:
        print(num)