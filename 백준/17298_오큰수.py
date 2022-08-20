

N = int(input())
nums = list(map(int, input().split()))

stack = [nums[-1]]
ans = [-1]

for i in range(N-2, -1, -1):
    if len(stack) != 0:
        n = nums[i]
        if stack[-1] > n:
            ans.append(stack[-1])
            stack.append(n)
        elif stack[-1] <= nums[i]:
            while True:
                if len(stack) == 0:
                    stack.append(n)
                    ans.append(-1)
                    break
                elif stack[-1] <= nums[i]:
                    stack.pop()
                else:
                    ans.append(stack[-1])
                    stack.append(n)
                    break
    else:
        stack.append(nums[i])
        ans.append(-1)

print(*ans[::-1])