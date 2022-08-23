def pop():
    global top
    top -= 1
    return stack[top + 1]

def push(x):
    global top
    top += 1
    stack[top] = x

for t in range(1, 11):
    icp = {'*': 2 , '/': 2, '+': 1, '-': 1, '(': 3, ')': 4}
    isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}

    N = int(input())
    nums = input()
    stack = [0] * N
    top = -1
    ans = []


    for i in nums:
        if i not in icp:        #숫자는 바로 ans에 넣기
            ans += [int(i)]
        else:
            if icp[i] > 3:
                while top != -1:
                    if isp[stack[top]] == 0:      #0일 때 (여는 가로)
                        pop()
                        break
                    else:
                        ans += [pop()]
            else:
                while top != -1:
                    if icp[i] > isp[stack[top]]:       #클 경우
                        push(i)
                        break
                    elif icp[i] <= isp[stack[top]]:
                        ans += [pop()]
                if top == -1:
                    push(i)
    else:
        while top != -1:
            ans += pop()
        top = -1

    for i in ans:
        if i not in icp:
            push(i)
        else:
            nums1, nums2 = pop(), pop()
            if i == '*':
                push(nums1 * nums2)
            else:
                push(nums1 + nums2)

    print(f'#{t}', stack[0])





