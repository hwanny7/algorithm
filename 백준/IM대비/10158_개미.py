import sys

W, H = map(int, sys.stdin.readline().split())
r, c = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())

a = (r + t) % W
b = (c + t) % H

if ((r + t) // W) % 2:      #홀수
    ans_x = W - a
else:
    ans_x = 0 + a
if ((c + t) // H) % 2:
    ans_y = H - b
else:
    ans_y = 0 + b

print(ans_x, ans_y)