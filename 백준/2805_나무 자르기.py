# N , M = map(int, input().split())
# nums = list(map(int, input().split()))
#
# start = 0
# end = sum(nums)
#
# while start <= end:
#     middle = (start + end) // 2
#     total = 0
#     for i in nums:
#         if i < middle:
#             continue
#         total += i - middle
#
#     if total == M:
#         print(middle)
#         break
#     elif total < M:
#         end = middle - 1
#     else:
#         start = middle + 1

N , M = map(int, input().split())
nums = list(map(int, input().split()))

start = 0
end = max(nums)

while start <= end:
    middle = (start + end) // 2
    total = 0
    for i in nums:
        if i < middle:
            continue
        total += i - middle
        if total == M:
            break

    if total == M:
        print(middle)
        break
    elif total < M:
        end = middle - 1
    else:
        start = middle + 1