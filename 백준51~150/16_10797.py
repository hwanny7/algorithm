n = int(input())

lst = [i for i in list(map(int, input().split())) if i == n ]
print(len(lst))