#
# for t in range(1, int(input()) + 1):
#     n = int(input())
#     m = round(n ** (1/3))
#     print(f'#{t}', m) if n == m ** 3 else print(f'#{t}', -1)



while True:
    N = input()
    if N == '#':
        break
    N = list(N)
    total = 0
    for i in N:
        if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            total += 1
    print(total)