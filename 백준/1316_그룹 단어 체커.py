

n = int(input())
count = 0
for i in range(n):
    word = input()
    dic = {word[0]:0}
    for j in range(1, len(word)):
        if word[j] in dic and word[j-1] != word[j]:
            break
        else:
            dic[word[j]] = 0
    else:
        count += 1

print(count)