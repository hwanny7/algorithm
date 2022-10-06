<<<<<<< HEAD
def find(used = 0):




    for i in range(len(plan) - 2):



for t in range(1, int(input()) + 1):
    day, mon, three, year = map(int, input().split())
    plan = input().split()
    plan = ''.join(plan).strip('0')
=======
#============================dp 버전

for t in range(1, int(input()) + 1):
    day, mon, three, year = map(int, input().split())
    plan = [0] + list(map(int, input().split()))
    dp = [0] * 13

    for i in range(1, 13):
        dp[i] = min(dp[i - 1] + min(plan[i] * day, mon), dp[i - 3] + three)

    print(f'#{t}', dp[12] if dp[12] < year else year)
    print(dp)


# def find(lst, idx = 0, total = 0):
#     global ans
#
#     if total >= ans:
#         return
#
#     if idx >= l - 2:
#         ans = min(total, ans)
#         return
#
#     if lst[idx] + lst[idx + 1] + lst[idx + 2] > three:
#         find(lst, idx + 3, total + three)
#     find(lst, idx + 1, total + lst[idx])
#
# for t in range(1, int(input()) + 1):
#     day, mon, three, year = map(int, input().split())
#     plan = list(map(int, input().split()))
#     plan += [0] * 2
#     l = len(plan)
#     ans = year
#
#     for i in range(len(plan)):
#         a = plan[i] * day
#         if a >= mon:
#             plan[i] = mon
#         else:
#             plan[i] = a
#
#     find(plan)
#     print(f'#{t}', ans)
>>>>>>> b0336cb9ac0b272cc68631c4d9c8adf4503dc3ee
