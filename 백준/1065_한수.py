
n = input()
count = 99
while True:
    if len(list(map(int, n))) == 1 or len(list(map(int, n))) == 2:
        print(n)
        break
    else:
        for i in range(110, int(n)+1):
            sub = set()
            n = list(map(int, str(i)))
            for j in range(0, len(n)-1):
                sub.add(n[j] - n[j+1])
            if len(sub) == 1:
                count += 1
        print(count)
        break





