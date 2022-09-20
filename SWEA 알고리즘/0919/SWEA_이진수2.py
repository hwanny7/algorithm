def prime(x):
    global ans
    if x == 0.0:
        return
    ans += str(int(x * 2))
    prime(x * 2 - int(x * 2))

for t in range(1, int(input()) +1):
    N = float(input())
    ans = ''
    prime(N)
    if len(ans) >= 13:
        print(f'#{t}', 'overflow')
    else:
        print(f'#{t}', ans)
