for t in range(1, int(input())+1):
    x = input()
    s = input()
    for i in range(len(s)-len(x)+1):
        if s[i] == x[0]:
            if x == s[i:i+len(x)]:
                print(f'#{t}', 1)
                break
    else:
        print(f'#{t}', 0)