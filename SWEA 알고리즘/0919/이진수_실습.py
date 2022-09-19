arr = '0000000111100000011000000111100110000110000111100111100111111001100111'

for i in range(0, len(arr), 7):
    # print(arr[i:i + 7], int(arr[i:i + 7], 2))
    num = 0
    for j in range(i, i + 7):
        num = num * 2     # 2진수이므로
        if arr[j] == '1':
            num += 1
    print(num)
    1111000

    # for j in range(7):
    #     if arr[i + j] == '1':
    #         num = num | (1 << (6 - j))
    # print(num, end=' ')
