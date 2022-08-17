n_lst = []
for i in range(9):
  n = int(input())
  n_lst.append(n)

a = max(n_lst)
print(max(n_lst))
print(n_lst.index(a)+1)