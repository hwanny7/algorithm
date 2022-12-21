from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
ans = deque()
for i in range(N):
    command = input().rstrip()
    long = len(ans)
    if command == 'front':
        print(ans[0] if long else -1)
    elif command == 'back':
        print(ans[-1] if long else -1)
    elif command == 'size':
        print(long)
    elif command == 'pop_front':
        print(ans.popleft() if long else -1)
    elif command == 'pop_back':
        print(ans.pop() if long else -1)
    elif command == 'empty':
        print(0 if long else 1)
    elif command[:6] =='push_b':
        ans.append(command.split(' ')[1])
    elif command[:6] =='push_f':
        ans.appendleft(command.split(' ')[1])