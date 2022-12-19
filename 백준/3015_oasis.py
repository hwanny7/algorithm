


import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    arr = [int(sys.stdin.readline()) for _ in range(N)]
    stack = []
    ans = 0

    for i in range(N):

        while stack and stack[-1][0] < arr[i]:
            ans += stack[-1][1]
            stack.pop()

        if stack:
            if stack[-1][0] == arr[i]:
                temp = stack.pop()[1]
                if stack:
                    ans += 1
                ans += temp
                stack.append([arr[i], temp + 1])
            else:   # 나보다 큰 경우
                ans += 1
                stack.append([arr[i], 1])
        else:
            stack.append([arr[i], 1])

    print(ans)