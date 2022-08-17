
n = input()
lst = []
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in alpha:
    for j in range(len(n)):
        if i == n[j]:
            lst.append(j)
            break
    else:
        lst.append(-1)
print(*lst)
