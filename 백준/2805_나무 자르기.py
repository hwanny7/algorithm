

# N, M = map(int, input().split())
#
# nums = list(map(int, input().split()))
#
#
# start = 1
# end = max(nums)
# ans = 0
# while start <= end and ans == 0:
#     middle = (start + end) // 2
#     total = 0
#     for i in nums:
#         if i > middle:
#             total += i - middle
#     if total == M:
#         print(middle)
#         ans = middle
#         break
#
#     if total > M:
#         start = middle + 1
#     else:
#         end = middle - 1


N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)  # 이분탐색 검색 범위 설정

while start <= end:  # 적절한 벌목 높이를 찾는 알고리즘
    mid = (start + end) // 2

    log = 0  # 벌목된 나무 총합
    for i in tree:
        if i >= mid:
            log += i - mid

    # 벌목 높이를 이분탐색
    if log >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)